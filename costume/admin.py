from django.contrib import admin

# Register your models here.
from .models import CostumeProduct, CostumeCategory

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'parent_category', 'name', 'slug']
    prepopulated_fields = {'slug':('name',)} # slug 자동설정


admin.site.register(CostumeCategory, CategoryAdmin)


class ProduckAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'name', 'price', 'stock']
    list_editable = ['price', 'stock']

admin.site.register(CostumeProduct, ProduckAdmin)