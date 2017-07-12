from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # ex: //
    url(r'^$', views.CompanyView.as_view()),

    url(r'^sub/', views.SubcontactsView.as_view()),

    url(r'^create/', views.CompanyCreateAPIView.as_view())

    # ex: /polls/5/
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]


urlpatterns = format_suffix_patterns(urlpatterns)