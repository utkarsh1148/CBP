from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import CCDatails
from . serializers import CCSerializer
import json
from rest_framework.generics import ListAPIView


class CCList(APIView):
    
    def get(self,request):
        CC1=CCDatails.objects.filter(Name='Utkarsh Mishra')
        serializer=CCSerializer(CC1,many=True)
        return Response(serializer.data)
        
    def post(self,request):
        res=json.loads(request.body)
        print(res)
        if(res['work']=='get'):
            name=res['Name']
            CC1=CCDatails.objects.filter(Name=name)
            serializer=CCSerializer(CC1,many=True)
            return Response(serializer.data)
        else:
            name=res['Name']
            CC1=CCDatails(CreditNum=res['creditnum'],ExipryDate=res['expirydate'],CVV=res['cvv'],Name=name)
            CC1.save()
            data = {
                    'name': 'Vitor',
                    'location': 'Finland',
                    'is_active': True,
                    'count': 28
                    }
            serializer = json.dumps(data)
            return Response(serializer,content_type='application/json')