from django.db import models

# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=20)
    home_image = models.ImageField(upload_to='home_preview_images/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return self.name