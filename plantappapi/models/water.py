from django.db import models


class Water(models.Model):

    water_needs = models.CharField(max_length=50)