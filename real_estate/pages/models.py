from collections.abc import Iterable
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class CaseModel(models.Model):
    """A model for all real estate files."""
    title = models.CharField(max_length=120)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images')
    image2 = models.ImageField(upload_to='images', null=True, blank=True, default=None)
    image3 = models.ImageField(upload_to='images', null=True, blank=True, default=None)
    image4 = models.ImageField(upload_to='images', null=True, blank=True, default=None)
    slug = models.SlugField(max_length=32, unique=True, allow_unicode=True, blank=True)
    # slug = models.UUIDField(default=uuid.uuid4, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        return super(CaseModel, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("file_page", kwargs={"slug": self.slug})
    
    
    