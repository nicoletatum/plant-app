from django.db import models


class Water(models.Model):

    amount = models.CharField(max_length=50)