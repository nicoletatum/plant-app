# from django.db.models.deletion import SET_DEFAULT
# from django.db.models.query import FlatValuesListIterable
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.conf import settings
from plantappapi.models import Plant, PlantOwner, Light, Water
import cloudinary


class PlantView(ViewSet):
    """ plants """
    cloudinary.config(
            cloud_name=settings.CLOUDINARY_STORAGE['CLOUD_NAME'],
            api_key=settings.CLOUDINARY_STORAGE['API_KEY'],
            api_secret=settings.CLOUDINARY_STORAGE['API_SECRET'])

    def create(self, request):

        #uses token passed in 'auth' header
        plant_owner = PlantOwner.objects.get(user=request.auth.user)
        light_level = Light.objects.get(pk=request.data["light_level"])
        water_needs = Water.objects.get(pk=request.data["water_amount"])

        #create new plant class instance
        #and set properties from what was sent
        plant = Plant()
        plant.name = request.data["name"]
        plant.light_level = light_level
        plant.water_amount = water_needs
        plant.temp_needs = request.data["temp_needs"]
        plant.potting_needs = request.data["potting_needs"]
        plant.plant_owner = plant_owner
        plant.notes = request.data["notes"]
        if request.data["plant_pic"] !="":
            plant.plant_pic = cloudinary.uploader.upload(request.data['plant_pic'])['url']
        if request.data["last_water"] !="":
            plant.last_water = request.data["last_water"]

        try:
            plant.save()
            serializer = PlantSerializer(plant, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        """ handles GET request """
        try: 
            plant = Plant.objects.get(pk=pk)
            serializer = PlantSerializer(plant, context={'request': request})
            return Response(serializer.data)
        except Exception as ex: 
            return HttpResponseServerError(ex)

    def update(self,request, pk=None):     
        #uses token passed in 'auth' header
        plant_owner = PlantOwner.objects.get(user=request.auth.user)
        light_level = Light.objects.get(pk=request.data["light_level"])
        water_needs = Water.objects.get(pk=request.data["water_amount"])

        plant = Plant.objects.get(pk=pk)
        plant.name = request.data["name"]
        plant.light_level = light_level
        plant.water_amount = water_needs
        plant.temp_needs = request.data["temp_needs"]
        plant.potting_needs = request.data["potting_needs"]
        plant.plant_owner = plant_owner
        plant.notes = request.data["notes"]
        if request.data["plant_pic"] !="":
            plant.plant_pic = cloudinary.uploader.upload(request.data['plant_pic'])['url']
        plant.pest_watch = request.data["pest_watch"]
        if request.data["last_water"] !="":
            plant.last_water = request.data["last_water"]

        plant.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)


    def destroy(self, request, pk=None):
        
        try:
            plant = Plant.objects.get(pk=pk)
            plant.delete()

            return Response({}, status= status.HTTP_204_NO_CONTENT)

        except Plant.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    


    def list(self, request):

        plant = Plant.objects.filter(plant_owner=PlantOwner.objects.get(user=request.auth.user)).order_by("-pest_watch")

        serializer = PlantSerializer(
            plant, many=True, context={'request': request})
        return Response(serializer.data)

class LightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Light
        fields = ('id', 'level')

class WaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Water
        fields = ('id', 'amount')

class PlantSerializer(serializers.ModelSerializer):
    light_level = LightSerializer(many=False)
    water_amount = WaterSerializer(many=False)
    class Meta:
        model = Plant
        fields = ('id', 'name', 'plant_pic', 'last_water', 'pest_watch', 'light_level', 'water_amount', 'temp_needs', 'potting_needs', 'plant_owner', 'notes')
