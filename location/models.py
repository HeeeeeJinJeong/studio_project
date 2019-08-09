from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField

class Location(models.Model):
    title = models.CharField(max_length=50)
    description = RichTextField()

    def __str__(self):
        return self.title