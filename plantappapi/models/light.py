from django.db import models
from django.contrib.auth.models import User


class light(models.Model):

    light_level = models.CharField(max_length=50)