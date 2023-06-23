from django.db import models
from django.contrib.auth.models import User


class WebAuthnCredential(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credential_id = models.TextField()
    public_key = models.TextField()
    sign_count = models.IntegerField()
