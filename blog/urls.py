from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.ingresar_variables),
    url(r'^resultado/(?P<result>[0-9]+)/$', views.resultado,  name='resultado')
]