from django.contrib import admin
from .models import (Light, Water, Plant, PlantOwner)

# Register your models here.
admin.site.register(Light)
admin.site.register(Water)
admin.site.register(Plant)
admin.site.register(PlantOwner)