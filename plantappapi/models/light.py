from django.db import models


class Light(models.Model):

    level = models.CharField(max_length=50)