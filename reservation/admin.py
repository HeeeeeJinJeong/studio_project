from django.contrib import admin

# Register your models here.
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['created', 'updated']
    search_fields = ['name']
    ordering = ['-updated', '-created']


admin.site.register(Reservation, ReservationAdmin)