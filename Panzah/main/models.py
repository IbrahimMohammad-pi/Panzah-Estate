from operator import mod
from re import T
from django.db import models


class LandLord(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tenant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    current_owner = models.ForeignKey(LandLord, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BuildingAddress(models.Model):
    building_name = models.CharField(max_length=100, blank=True)
    building_number = models.IntegerField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    county = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


class RentalProperties(models.Model):
    building_address = models.ForeignKey(to=BuildingAddress, on_delete=models.CASCADE)
    current_tenant = models.OneToOneField(
        to=Tenant,
        on_delete=models.SET_NULL,
        null=True,
    )
    current_owner = models.ForeignKey(to=LandLord, on_delete=models.SET_NULL, null=True)

    unit_number = models.IntegerField()
    floor_number = models.IntegerField()
    status = models.CharField(max_length=20)
    rent_amount = models.IntegerField()


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subcategories",
    )
