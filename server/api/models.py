from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    gender = models.CharField(max_length=15, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    activity = models.CharField(max_length=40,blank=True, null=True)

class IntakeData(models.Model):
    date = models.DateField()
    email = models.EmailField()
    time = models.CharField(max_length=20, blank=True, null=True)
    item = models.CharField(max_length=30, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    calorie = models.IntegerField(blank=True, null=True)
    proteins = models.DecimalField(decimal_places=1, max_digits=6, blank=True, null=True)
    carbs = models.DecimalField(decimal_places=1, max_digits=6, blank=True, null=True)
    fats = models.DecimalField(decimal_places=1, max_digits=6, blank=True, null=True)
    fiber = models.DecimalField(decimal_places=1, max_digits=6, blank=True, null=True)

class FoodData(models.Model):
    item = models.CharField(max_length=30)
    calories = models.IntegerField()
    proteins = models.DecimalField(decimal_places=1, max_digits=6, blank=True, null=True)
    carbs = models.DecimalField(decimal_places=1, max_digits=6, blank=True, null=True)
    fats = models.DecimalField(decimal_places=1, max_digits=6, blank=True, null=True)
    fiber = models.DecimalField(decimal_places=1, max_digits=6, blank=True, null=True)

class WaterConsumption(models.Model):
    email = models.EmailField(max_length=50)
    date = models.DateField()
    counts = models.IntegerField()