from django.contrib import admin
from driverslog.models import Vehicle, Fuel, Purchase, PurchaseType, Maintenance, Part, Trip
#from django.contrib.admin.helpers import Fieldset

admin.site.register(Vehicle)
admin.site.register(Fuel)
admin.site.register(Purchase)
admin.site.register(PurchaseType)
admin.site.register(Maintenance)
admin.site.register(Part)
admin.site.register(Trip)