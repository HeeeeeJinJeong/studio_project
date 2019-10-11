from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class Reservation(models.Model):
    title = models.CharField(max_length=50)

    name = models.CharField(max_length=30)
    email = models.EmailField()

    date_to = models.DateTimeField(default=timezone.now)
    date_from = models.DateTimeField('Date')

    num_people = models.IntegerField()
    amount = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    rental = models.CharField(max_length=200, blank=True)
    password = models.CharField(max_length=30)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('reservation:detail', args=[self.id])