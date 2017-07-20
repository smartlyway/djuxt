from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views, serializers
from .models import Package, Company
from rest_framework.views import *
from rest_framework.generics import *

urlpatterns = [
    # ex: //
    # url(r'^$', views.CompanyView.as_view()),

    url(r'company/(?P<pk>\d+)/', RetrieveUpdateDestroyAPIView.as_view(queryset=Company.objects.all(),
                                               serializer_class=serializers.CompanySerializer)),


    url(r'company/all/', ListCreateAPIView.as_view(queryset=Company.objects.all(),
                                               serializer_class=serializers.CompanySerializer)),

    url(r'company/three/', ListCreateAPIView.as_view(queryset=Company.objects.all(),
                                                   serializer_class=serializers.CompanyThreeSerializer)),


    url(r'package', RetrieveUpdateDestroyAPIView.as_view(queryset=Package.objects.all(),
                                               serializer_class=serializers.PackageSerializer)),

    url(r'package/all/', ListAPIView.as_view(queryset=Package.objects.all(),
                                               serializer_class=serializers.PackageSerializer))

    # ex: /polls/5/
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]


# urlpatterns = format_suffix_patterns(urlpatterns)