from django.db import models


class Window(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=100, default="")
    elementId = models.CharField(max_length=100, default="")
    title = models.CharField(max_length=100, default="", blank=True)
    top = models.IntegerField(default=0)
    left = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

    
