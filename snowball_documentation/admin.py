from markdownx.admin import MarkdownxModelAdmin
from django.contrib import admin
from .models import Documentation

admin.site.register(Documentation, MarkdownxModelAdmin)
