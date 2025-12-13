from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.safestring import mark_safe
from phonenumber_field.modelfields import PhoneNumberField
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill

from core.settings import MEDIA_ROOT


class User(AbstractUser):
    phone = PhoneNumberField(verbose_name='Phone', blank=True, null=True)
    image = ProcessedImageField(
        verbose_name='Image',
        upload_to='user/',
        processors=[],
        null=True,
        blank=True
    )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(200, 200)]
    )
    about = models.TextField(verbose_name='About me', null=True, blank=True)

    # Why is it kostil
    def image_tag_thumbnail(self):
        if self.image:
            if not self.image_thumbnail:
                User.objects.get(id=self.id)
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image_thumbnail}' width='70'>")

    image_tag_thumbnail.short_description = 'Current profile picture'

    def image_tag(self):
        if self.image:
            if not self.image_thumbnail:
                User.objects.get(id=self.id)
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image_thumbnail}'>")

    image_tag.short_description = 'Current profile picture'
