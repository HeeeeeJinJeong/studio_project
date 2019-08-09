from django.contrib import admin

# Register your models here.
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'time']
    list_filter = ['created', 'updated']
    search_fields = ['name']
    ordering = ['-updated', '-created']


admin.site.register(Appointment, AppointmentAdmin)