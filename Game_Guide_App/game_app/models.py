from django.db import models
from pytils.translit import slugify

class Gamedesc(models.Model):
    title = models.CharField("Game name", max_length=255)
    date = models.CharField("Game name", max_length=255)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)