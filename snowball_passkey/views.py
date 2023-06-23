from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import WebAuthnCredential
from django.utils.crypto import get_random_string
import webauthn

RP_ID = "0.0.0.0:8000"
RP_ORIGIN = "http://0.0.0.0:8000"


@login_required
@csrf_exempt
def begin_registration(request):
    # Check if the user has already registered
    if WebAuthnCredential.objects.filter(user=request.user).exists():
        return JsonResponse({"error": "User has already registered."}, status=400)

    # Generate a random challenge and save it in the session
    challenge = get_random_string(32)
    request.session["challenge"] = challenge

    return JsonResponse({"challenge": challenge})


@login_required
@csrf_exempt
def finish_registration(request):
    credential = request.POST.get("credential")

    # Get the challenge from the session
    challenge = request.session.get("challenge")

    # Verify the registration response
    webauthn_registration_response = webauthn.WebAuthnRegistrationResponse(
        RP_ID,
        RP_ORIGIN,
        credential,
        challenge,
        trusted_attestation_cert_required=True,
        self_attestation_permitted=False,
        none_attestation_permitted=False,
    )
    webauthn_credential = webauthn_registration_response.verify()

    print(webauthn_credential)

    # Save the credential in the database
    WebAuthnCredential.objects.create(
        user=request.user,
        credential_id=webauthn_credential.credential_id,
        public_key=webauthn_credential.public_key,
        sign_count=webauthn_credential.sign_count,
    )

    return JsonResponse({"status": "Registration successful."})


@login_required
@csrf_exempt
def begin_authentication(request):
    credential = WebAuthnCredential.objects.get(user=request.user)

    # Generate a random challenge and save it in the session
    challenge = get_random_string(32)
    request.session["challenge"] = challenge

    return JsonResponse(
        {
            "challenge": challenge,
            "credential_id": credential.credential_id,
        }
    )


@login_required
@csrf_exempt
def finish_authentication(request):
    credential_response = request.POST.get("credential")

    # Get the challenge from the session
    challenge = request.session.get("challenge")

    # Get the stored credential
    stored_credential = WebAuthnCredential.objects.get(user=request.user)

    # Verify the authentication response
    webauthn_user = webauthn.WebAuthnUser(
        stored_credential.user.id,
        stored_credential.user.username,
        stored_credential.user.username,
        stored_credential.user.username,
        stored_credential.credential_id,
        stored_credential.public_key,
        stored_credential.sign_count,
        RP_ID,
    )
    webauthn_assertion_response = webauthn.WebAuthnAssertionResponse(
        webauthn_user, credential_response, challenge, RP_ORIGIN, uv_required=False
    )
    webauthn_user = webauthn_assertion_response.verify()

    # Update the sign count
    stored_credential.sign_count = webauthn_user.sign_count
    stored_credential.save()

    return JsonResponse({"status": "Authentication successful."})
