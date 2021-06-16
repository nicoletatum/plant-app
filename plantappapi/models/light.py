from django.db import models


class Light(models.Model):

    light_level = models.CharField(max_length=50)