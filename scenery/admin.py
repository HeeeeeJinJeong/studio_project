from django.contrib import admin

# Register your models here.
from .models import Scenery, SceneryCategory

class SceneryCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'parent_category', 'name', 'slug', 'category_image']
    prepopulated_fields = {'slug': ('name',)}  # slug 자동설정

admin.site.register(SceneryCategory, SceneryCategoryAdmin)


class SceneryViewAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'slug']

admin.site.register(Scenery, SceneryViewAdmin)