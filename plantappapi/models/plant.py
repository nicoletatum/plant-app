from django.db import models


class Plant(models.Model):
    
    name = models.CharField(max_length=50)
    light_level = models.ForeignKey("Light", on_delete=models.CASCADE)
    water_needs = models.ForeignKey("Water", on_delete=models.CASCADE)
    plant_owner = models.ForeignKey("PlantOwner", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    potting_needs = models.CharField(max_length=200)
    temp_needs = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    plant_pic = models.ImageField(
        upload_to='plantimage', height_field=None,
        width_field=None, max_length=None, null=True)