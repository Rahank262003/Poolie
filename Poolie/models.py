from django.db import models
from decimal import Decimal
from django.utils import timezone


class Registration(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    license_no = models.CharField(max_length=50, null=True, blank=True)
    insurance_no = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Publishride(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    seats = models.IntegerField()
    contact_number = models.CharField(max_length=15, default='')
    email = models.EmailField(max_length=254,default='')
    date_of_journey = models.DateField(default=timezone.now)
    time_of_journey = models.TimeField(null=True, blank=True)
    cost_per_seat = models.DecimalField(
        max_digits=5, decimal_places=2, default='0.00')
    gender = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.source + self.contact_number


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Passenger(models.Model):
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    seats = models.IntegerField()
    date_of_journey = models.DateField()

    def __str__(self):
        return self.email
    