from django.db import models

class Category(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=128)
    justification = models.CharField(max_length=128)
    longitude = models.IntegerField(null=True)
    latitude = models.IntegerField(null=True)
    ares_hectares = IntegerField(null=True)
    states = models.CharField(max_length=128)
    region = models.CharField(max_length=128)
    iso = models.CharField(max_length=128)

    def __str__(self) :
        return self.name, self.year, self.category, self.description, self.justification, self.longitude, self.latitude, self.area_hectares, self.states, self.region, self.iso
