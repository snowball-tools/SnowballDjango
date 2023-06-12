from markdownx.models import MarkdownxField
from django.db import models

TECHNOLOGY_CHOICES = [
    ("SW", "SwiftUI"),
    ("RE", "React"),
    ("JP", "Jetpack"),
]


class Documentation(models.Model):
    component = models.CharField(max_length=255)
    technology = models.CharField(
        max_length=2,
        choices=TECHNOLOGY_CHOICES,
        default="SW",
    )
    content = MarkdownxField()

    def __str__(self):
        return f"{self.get_technology_display()} - {self.component}"
