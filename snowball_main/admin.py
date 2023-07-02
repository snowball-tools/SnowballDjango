from django.contrib import admin
from .models import Window


class WindowAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "url", "elementId", "style", "contents")

    prepopulated_field = {"elementId": ("name",)}


admin.site.register(Window, WindowAdmin)
