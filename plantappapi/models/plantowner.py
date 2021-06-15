from django.db import models
from django.contrib.auth.models import User


class PlantOwner(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)