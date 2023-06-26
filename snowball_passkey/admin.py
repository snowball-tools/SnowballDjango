from django.contrib import admin

from .models import SnowballAuth


@admin.register(SnowballAuth)
class SnowballAuthAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "created_on", "last_used_on"]
    search_fields = ["name", "credential_id"]
