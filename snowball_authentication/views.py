from django.shortcuts import render
from allauth.socialaccount.providers.apple.views import (
    AppleOAuth2Adapter,
    AppleOAuth2Client,
    AppleProvider,
)
from dj_rest_auth.registration.views import SocialLoginView as AppleLoginView


class AppleLogin(AppleLoginView):
    adapter_class = AppleOAuth2Adapter
    callback_url = "https://www.snowballtools.xyz/accounts/apple/login/callback"
    client_class = AppleOAuth2Client
