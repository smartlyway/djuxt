from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import *
from rest_framework.generics import *
import urllib
import json
from .models import Company, Address
from .serializers import *
from django.core import serializers


'''class ExampleView(View):
    @staticmethod
    def get(request):
        companies = Company.objects.all()

        return render(request, 'index.html', context={
            'title': 'Mi primera página con Django',
            'companies': companies,
        })'''


class CompaniesView(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = PackageSerializer

class PackagesView(RetrieveUpdateDestroyAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


class SubcontactsView(APIView):
    @staticmethod
    def get(request):
        address = SubContracts.objects.all()
        ser = SubContractsSerializer(address, many=True)
        return Response(ser.data)
