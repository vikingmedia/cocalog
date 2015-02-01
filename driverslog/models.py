from django.db import models
from django.contrib.auth.models import User


class Vehicle(models.Model):
    
    name = models.CharField(max_length=255)
    tachometer_max_value = models.PositiveIntegerField()
    
    def __unicode__(self):
        return self.name


class Trip(models.Model):
    
    TYPE_CHOICES = (
        ('privat', 'privat'),
        ('dienst', 'dienstlich'),
    )
    
    date = models.DateField()
    date_arrival = models.DateField(null=True)
    type = models.CharField(max_length=6, choices=TYPE_CHOICES)
    location_start = models.CharField(max_length=255, blank=True)
    location_destination = models.CharField(max_length=255)
    milage_start = models.PositiveIntegerField()
    milage_end = models.PositiveIntegerField()
    comment = models.CharField(max_length=255, blank=True)
    members = models.ManyToManyField(User)
    vehicle = models.ForeignKey('Vehicle')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
class Fuel(models.Model):
    
    date = models.DateField()
    liters = models.FloatField(null=True)
    amount = models.FloatField()
    full = models.BooleanField(default=False)
    comment = models.CharField(max_length=255, blank=True)
    member = models.ForeignKey(User)
    vehicle = models.ForeignKey('Vehicle')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return u'%s %s: %s [%s]' % (self.member.first_name, self.member.last_name, self.amount, self.date)
    
    
class Purchase(models.Model):
    
    date = models.DateField()
    amount = models.FloatField()
    type = models.ForeignKey('PurchaseType')
    description = models.CharField(max_length=255)
    member = models.ForeignKey(User)
    vehicle = models.ForeignKey('Vehicle')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.description
    
    
class PurchaseType(models.Model):
    
    name = models.CharField(max_length=255)
    community = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name
    
    
class Maintenance(models.Model):
    
    TYPE_CHOICES = (
        ('checked', 'kontrolliert'),
        ('resolved', 'behoben'),
    )
    
    part = models.ForeignKey('Part')
    milage = models.PositiveIntegerField()
    type = models.CharField(max_length=8, choices=TYPE_CHOICES)
    member = models.ForeignKey(User)
    comment = models.CharField(max_length=255)
    vehicle = models.ForeignKey('Vehicle')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
class Part(models.Model):
    
    name = models.CharField(max_length=255)
    maintenance_interval_time = models.PositiveIntegerField()
    maintenance_interval_mileage = models.PositiveIntegerField()
    comment = models.CharField(max_length=255, blank=True)
    vehicle = models.ForeignKey('Vehicle')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name
    