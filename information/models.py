from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField

class Information(models.Model):
    information_title = models.CharField(max_length=30, blank=True, null=True)
    information_text = RichTextField()
    information_image = models.ImageField(upload_to='information_images/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return self.information_title