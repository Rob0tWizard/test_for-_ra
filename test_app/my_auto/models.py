from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
