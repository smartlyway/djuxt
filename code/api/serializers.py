from rest_framework import serializers
from .models import *


def update_model(serializer, data, instance, ignore = [], save = True):
    '''
    Update data of the model with the user data.
    :param serializer: Serializer of the model
    :param data: data to add
    :param instance: instance of model
    :param ignore: fields to ignore
    :param save: if perist the instance on db
    :return:
    '''
    for field in serializer.Meta.fields:
        if field not in ignore:
            setattr(instance, field, data.get(field))
    if save:
        instance.save()

    return instance


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('country', 'region', 'locality', 'street', 'number')

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ('name', 'max_subcompanies')

class TypeSerializer(serializers.ModelSerializer):
    package = PackageSerializer(read_only=True, many=True)
    class Meta:
        model = Type
        fields = ('name', 'package')

class CompanySerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=False)
    type = TypeSerializer(many=False)
    lookup_field = 'nif'
    class Meta:
        model = Company
        fields = ('name', 'nif', 'address','phone','activity','type')

    def validate_name(self, value):
        if value == 'MyCompany':
            raise serializers.ValidationError('El nombre de la empresa debe ser MyCompany')
        return value

    def update(self, instance, v_data):
        update_model(AddressSerializer, v_data.pop('address'), instance.address)
        update_model(TypeSerializer, v_data.pop('type'), instance.type, ['package'])
        update_model(CompanySerializer, v_data, instance, ['type', 'address'])

        return instance



class CompanyThreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('pk','name', 'nif', 'address','phone','activity','type', 'childs')
        depth = 2



class SubContractsSerializer(serializers.ModelSerializer):
    parent = CompanySerializer(read_only=True, many=False)
    child = CompanySerializer(read_only=True, many=False)
    class Meta:
        model = SubContracts
        fields = ('parent', 'child')


