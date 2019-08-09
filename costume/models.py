from django.db import models

# Create your models here.
from django.urls import reverse
from ckeditor.fields import RichTextField

class CostumeCategory(models.Model):
    parent_category = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True, related_name='sub_categories')
    slug = models.SlugField(max_length=120, unique=True, allow_unicode=True, db_index=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('costume:product_in_category', args=[self.slug])

class CostumeProduct(models.Model):
    category = models.ForeignKey(CostumeCategory, on_delete=models.SET_NULL, blank=True, null=True, related_name='products')

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='product_images/%Y/%m/%d', blank=True, null=True)
    description = RichTextField(blank=True)

    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()

    def __str__(self):
        return "[" + self.category.name + "] " + self.name

    def get_absolute_url(self):
        return reverse('costume:detail', args=[self.id])