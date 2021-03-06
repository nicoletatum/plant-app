from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=50)
    light_level = models.ForeignKey("Light", on_delete=models.CASCADE)
    water_amount = models.ForeignKey("Water", on_delete=models.CASCADE)
    plant_owner = models.ForeignKey("PlantOwner", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    potting_needs = models.CharField(max_length=200)
    temp_needs = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    plant_pic = models.URLField(null=True)
    pest_watch = models.BooleanField(default=False)
    last_water = models.DateField()