from multiprocessing.connection import deliver_challenge
from django.db import models
from django.shortcuts import reverse
# Create your models here.
#Models for courier management system

class Courier(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    description = models.TextField()
    recipent_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    delivery_time = models.DateTimeField()
    delivery_address = models.CharField(max_length=100)
    notes = models.TextField()
    status = models.CharField(max_length=100, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.description)

    def get_absolute_url(self):
        return reverse('Delivery:couriers')



