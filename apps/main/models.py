from django.db import models

class Page(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(unique=True)
    text = models.TextField(max_length=255)
