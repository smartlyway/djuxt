from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import *
from rest_framework.generics import *

from .models import Company, Address
from .serializers import *
from django.core import serializers


class CompanyView(APIView):

    def get(self, request):
        address = Company.objects.all()
        ser = CompanyThreeSerializer(address, many=True)
        return Response(ser.data)

class CompanyCreateAPIView(CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class SubcontactsView(APIView):
    def get(self, request):
        address = SubContracts.objects.all()
        ser = SubContractsSerializer(address, many=True)
        return Response(ser.data)