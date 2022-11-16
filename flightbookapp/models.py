from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class personal_det(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE ,null=True, blank=True)
    address = models.TextField(max_length=200, null=False)
    phonenum = models.TextField(max_length=20, null=False)

class flight_details(models.Model):
    flight_code = models.TextField(max_length=20, primary_key=True)
    airline = models.TextField(max_length=100,null=False)
    source = models.TextField(max_length=100,null=False)
    destination = models.TextField(max_length=100,null=False)
    dep_date = models.DateTimeField(null=False)
    arrival_date = models.DateTimeField(null=False)
    price = models.FloatField(null=False)
    tot_seat_count = models.IntegerField(default=60)
    vacc_count = models.IntegerField(default=60)


class Booking_det(models.Model):
    flight_code = models.ForeignKey(flight_details, on_delete=models.CASCADE, blank=True, null=False)
    username = models.TextField(max_length=200,null=False)

