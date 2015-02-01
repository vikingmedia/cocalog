from django.contrib import admin
from driverslog.models import Vehicle, Fuel
from django.contrib.admin.helpers import Fieldset

admin.site.register(Vehicle)
admin.site.register(Fuel)