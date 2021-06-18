from django.db.models import fields
from django.db.models.deletion import SET_DEFAULT
from django.http import HttpResponseServerError, response
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from plantappapi.models import Light

class LightView(ViewSet):

    def retrieve(self, request):


        try:
            light = Light.objects.get(pk=pk)
            serializer = LightSerializer(light, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)



    def list(self, request):

        light = Light.objects.all()

        serializer = LightSerializer(
            light, many=True, context={'request': request})            
        return Response(serializer.data)

class LightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Light
        fields = ('id', 'level')

