import logging
from base64 import b64decode, b64encode

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pydantic.error_wrappers import ValidationError
from webauthn import (
    generate_authentication_options,
    generate_registration_options,
    options_to_json,
    verify_registration_response,
)
from webauthn.helpers import generate_challenge
from webauthn.helpers.exceptions import InvalidRegistrationResponse
from webauthn.helpers.structs import (
    AttestationConveyancePreference,
    AuthenticationCredential,
    AuthenticatorSelectionCriteria,
    RegistrationCredential,
    ResidentKeyRequirement,
    UserVerificationRequirement,
)

from snowballwebapp import settings
from .models import SnowballAuth

logger = logging.getLogger(__name__)

User = get_user_model()

@csrf_exempt
@login_required
def register_begin(request):
    site = get_current_site(request)
    hostname = site.domain.split(":")[0]
    challenge = generate_challenge()
    request.session["challenge"] = b64encode(challenge).decode()
    registration_options = generate_registration_options(
        rp_id=hostname,
        rp_name=site.name,
        user_id=b64encode(str(request.user.id).encode()).decode(),
        user_name=request.user.get_username(),
        user_display_name=f"{site.name} user: {request.user.get_username()}",
        challenge=challenge,
        attestation=AttestationConveyancePreference.NONE,
        authenticator_selection=AuthenticatorSelectionCriteria(
            resident_key=ResidentKeyRequirement.REQUIRED,
            user_verification=UserVerificationRequirement.REQUIRED,
        ),
    )

    return HttpResponse(
        options_to_json(registration_options), content_type="application/json"
    )


@csrf_exempt
@login_required
def register_verify(request):
    site = get_current_site(request)
    hostname = site.domain.split(":")[0]
    encoded_challenge = request.session.get("challenge")
    if not encoded_challenge:
        return JsonResponse("No challenge exists in your session.", status=422)

    challenge = b64decode(encoded_challenge)

    try:
        credential = RegistrationCredential.parse_raw(request.POST)
    except ValidationError as e:
        messages.error(request, "Invalid authentication data.")
        if settings.DEBUG:
            logger.debug(f"{e}: {request.POST}")
        return redirect(settings.LOGIN_ERROR_URL)

    try:
        registration_verification = verify_registration_response(
            credential=credential,
            expected_challenge=challenge,
            expected_rp_id=hostname,
            expected_origin=f"https://{site.domain}",
            require_user_verification=True,
        )
    except InvalidRegistrationResponse as e:
        messages.error(request, "Registration failed. Error: {}".format(e))
        return redirect(settings.REGISTRATION_ERROR_URL)

    auth_data = SnowballAuth.objects.filter(
        credential_id=registration_verification.credential_id.decode()
    )
    if auth_data.exists():
        messages.error(
            request,
            "This key is already registered to an account. Try logging in with it.",
        )
        return redirect(settings.REGISTRATION_ERROR_URL)

    SnowballAuth.objects.create(
        user=request.user,
        credential_id=registration_verification.credential_id.decode(),
        public_key=registration_verification.credential_public_key.decode(),
    )
    messages.success(request, "Your key has been successfully registered.")
    return redirect(settings.REGISTRATION_REDIRECT_URL)


@csrf_exempt
def login_begin(request):
    site = get_current_site(request)
    hostname = site.domain.split(":")[0]
    challenge = generate_challenge()
    request.session["challenge"] = b64encode(challenge).decode()
    authentication_options = generate_authentication_options(
        rp_id=hostname,
        challenge=challenge,
        user_verification=UserVerificationRequirement.REQUIRED,
    )

    return HttpResponse(
        options_to_json(authentication_options), content_type="application/json"
    )


@csrf_exempt
def login_verify(request):
    encoded_challenge = request.session.get("challenge")
    if not encoded_challenge:
        messages.error(request, "No challenge exists for your session.")
        return redirect(settings.LOGIN_ERROR_URL)

    try:
        credential = AuthenticationCredential.parse_raw(request.POST)
    except ValidationError:
        messages.error(request, "Invalid authentication data.")
        return redirect(settings.LOGIN_ERROR_URL)

    user = authenticate(request, credential=credential)
    if user is None:
        messages.error(request, "Your credentials could not be validated.")
        return redirect(settings.LOGIN_ERROR_URL)

    login(request, user)

    messages.success(request, "You have been successfully logged in.")
    return redirect(settings.LOGIN_REDIRECT_URL)


@login_required
def rename_key(request):
    key = SnowballAuth.objects.filter(pk=request.POST["key_id"]).first()
    if not key or key.user != request.user:
        messages.error(request, "That key does not exist.")
    else:
        key.name = request.POST["name"]
        key.save()
        messages.success(request, "The key has been renamed.")
    return redirect(settings.REGISTRATION_REDIRECT_URL)


@login_required
def delete_key(request):
    key = SnowballAuth.objects.filter(pk=request.POST["key_id"]).first()
    if not key or key.user != request.user:
        messages.error(request, "That key does not exist.")
    else:
        key.delete()
        messages.success(request, "The key has been deleted.")
    return redirect(settings.REGISTRATION_REDIRECT_URL)
