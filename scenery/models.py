from django.db import models

# Create your models here.
from django.shortcuts import resolve_url
from ckeditor.fields import RichTextField

class SceneryCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, allow_unicode=True, db_index=True)
    category_image = models.ImageField(upload_to='room_category_images/%Y/%m/%d', blank=True, null=True)
    parent_category = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True, related_name='room_category')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return resolve_url('scenery:room_view_in_category', self.slug)

class Scenery(models.Model):
    category = models.ForeignKey(SceneryCategory, on_delete=models.SET_NULL, blank=True, null=True, related_name='rooms')
    slug = models.SlugField(max_length=120, unique=True, allow_unicode=True, db_index=True)
    description = RichTextField(blank=True, null=True)
    room_image = models.ImageField(upload_to='room_images/%Y/%m/%d', blank=True, null=True)
    room_image2 = models.ImageField(upload_to='room_images/%Y/%m/%d', blank=True, null=True)
    room_image3 = models.ImageField(upload_to='room_images/%Y/%m/%d', blank=True, null=True)
    room_image4 = models.ImageField(upload_to='room_images/%Y/%m/%d', blank=True, null=True)
    room_image5 = models.ImageField(upload_to='room_images/%Y/%m/%d', blank=True, null=True)
    room_image6 = models.ImageField(upload_to='room_images/%Y/%m/%d', blank=True, null=True)


    def __str__(self):
        return str(self.category)

    def get_absolute_url(self):
        return resolve_url('scenery:detail', self.slug)