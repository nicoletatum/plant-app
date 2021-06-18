from django.db.models import fields
from django.db.models.deletion import SET_DEFAULT
from django.http import HttpResponseServerError, response
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from plantappapi.models import Water

class WaterView(ViewSet):

    def retrieve(self, request):


        try:
            water = Water.objects.get(pk=pk)
            serializer = WaterSerializer(water, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)



    def list(self, request):

        water = Water.objects.all()

        serializer = WaterSerializer(
            water, many=True, context={'request': request})            
        return Response(serializer.data)

class WaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Water
        fields = ('id', 'amount')

