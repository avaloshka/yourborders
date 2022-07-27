from django.db import models


# Create your models here.
class Borders(models.Model):
    location = models.CharField(max_length=100)
    cars = models.CharField(max_length=100)
    buses = models.CharField(max_length=100)
    lorries = models.CharField(max_length=100)
    text = models.TextField(max_length=1600)
    time = models.TimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.location


class Polish(models.Model):
    location = models.CharField(max_length=100)
    lorries = models.CharField(max_length=100)
    buses = models.CharField(max_length=100)
    cars = models.CharField(max_length=100)
    time = models.TimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.location

class Feedback(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=20000)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name