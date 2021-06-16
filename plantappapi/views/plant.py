from django.http import HttpResponseServerError, response
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from plantappapi.models import Plant, PlantOwner

class PlantView(ViewSet):

    # def create(self, request):

    #     #uses token passed in 'auth' header
    #     plant = Plant.objects.get(user=request.auth.user)
        
    #     #create new plant class instance
    #     #and set properties from what was sent
    #     plant = Plant()
    #     plant.name = request.data["name"]
    #     plant.light_level = request.data["light_level"]
    #     plant.water_needs = request.data["water_needs"]
    #     plant.temp_needs = request.data["temp_needs"]
    #     plant.potting_needs = request.data["potting_needs"]
    #     plant.plant_owner = PlantOwner
    #     plant.notes = request.data["notes"]

    #     try:
    #         plant.save()
    #         serializer = PlantSerializer



#PICK BACK UP HERE. LEFT TUESDAY NIGHT WORKING ON GET/POST PLANT

    def retrieve(self, request, pk=None):

        try: 
            plant = Plant.objects.get(pk=pk)
            serializer = PlantSerializer(plant, context={'request': request})
            return Response(serializer.data)
        except Exception as ex: 
            return HttpResponseServerError(ex)

    def list(self, request):

        plant = Plant.objects.all()

        serializer = PlantSerializer(
            plant, many=True, context={'request': request})
        return Response(serializer.data)


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ('id', 'name', 'plant_pic', 'light_level', 'water_amount', 'temp_needs', 'potting_needs', 'plant_owner', 'notes')
        depth = 1
