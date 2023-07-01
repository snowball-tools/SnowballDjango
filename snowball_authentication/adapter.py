from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class SnowballSocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_auto_signup_allowed(self, request, sociallogin):
        # By returning True here, we skip the signup form
        return True
