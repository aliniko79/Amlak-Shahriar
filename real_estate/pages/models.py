from django.db import models
from django.urls import reverse


class CaseModel(models.Model):
    """A model for all real estate files."""
    title = models.CharField(max_length=120)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images')
    image2 = models.ImageField(upload_to='images', null=True, blank=True, default=None)
    image3 = models.ImageField(upload_to='images', null=True, blank=True, default=None)
    image4 = models.ImageField(upload_to='images', null=True, blank=True, default=None)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("file_page", kwargs={"pk": self.pk})
    