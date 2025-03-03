from django.contrib import admin
from .models import LandLord, Tenant, BuildingAddress, RentalProperties, Category

admin.site.register(LandLord)
admin.site.register(Tenant)
admin.site.register(BuildingAddress)
admin.site.register(RentalProperties)
admin.site.register(Category)
