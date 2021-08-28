from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    cities = models.JSONField(default=[])

class MainCities(models.Model):
    cities = models.JSONField(default=[])
