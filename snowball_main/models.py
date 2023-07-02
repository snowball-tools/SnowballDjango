from django.db import models


class Window(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=100, default="")
    elementId = models.CharField(max_length=100, default="")
    title = models.CharField(max_length=100, default="", blank=True)
    style = models.CharField(max_length=200, blank=True)
    contents = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
