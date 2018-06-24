from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.ingresar_variables),
    url(r'^resultado/$', views.resultado)
]