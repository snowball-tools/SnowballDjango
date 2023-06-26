from django.contrib.auth import get_user_model
from django.db import models
from django.utils.timezone import now


class SnowballAuth(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(
        max_length=200, blank=True, help_text="The user-friendly name for this key."
    )
    credential_id = models.CharField(max_length=300, unique=True)
    public_key = models.CharField(max_length=500)
    sign_count = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    last_used_on = models.DateTimeField(default=now)

    class Meta:
        verbose_name_plural = "auth data"

    def set_sign_count(self, sign_count: int) -> None:
        self.sign_count = sign_count
        self.last_used_on = now()
        self.save()

    def __str__(self):
        return self.name or str(self.user)
