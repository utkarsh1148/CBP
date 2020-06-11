from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import CCDatails
from . serializers import CCSerializer


class CCList(APIView):
    
    def get(self,request):
        CC1=CCDatails.objects.all()
        serializer=CCSerializer(CC1,many=True)
        return Response(serializer.data)
        
    def post(self):
        pass