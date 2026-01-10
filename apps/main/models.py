from django.db import models
from tinymce.models import HTMLField
from apps.main.mixins import MetaTagMixin


class Page(MetaTagMixin):
    name = models.CharField(verbose_name='Name', max_length=255)
    slug = models.CharField(unique=True)
    text = HTMLField(verbose_name='Content', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Informational page'
        verbose_name_plural = 'Informational pages'
