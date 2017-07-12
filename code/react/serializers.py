from rest_framework import serializers
from .models import *

class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('country', 'region', 'locality', 'steet', 'number')

class PackageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Package
        fields = ('name', 'max_subcompanies')

class TypeSerializer(serializers.ModelSerializer):
    package = PackageSerializer(read_only=True, many=True)
    class Meta:
        model = Type
        fields = ('name', 'package')

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True, many=False)
    type = TypeSerializer(read_only=True, many=False)
    class Meta:
        model = Company
        fields = ('name', 'nif', 'address','phone','activity','type')

class CompanyThreeSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True, many=False)
    type = TypeSerializer(read_only=True, many=False)
    childs = CompanySerializer(read_only=True, many=True)
    class Meta:
        model = Company
        fields = ('name', 'nif', 'address','phone','activity','type', 'childs')

class SubContractsSerializer(serializers.ModelSerializer):
    parent = CompanySerializer(read_only=True, many=False)
    child = CompanySerializer(read_only=True, many=False)
    class Meta:
        model = SubContracts
        fields = ('parent', 'child')


