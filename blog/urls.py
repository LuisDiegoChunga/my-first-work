from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.plantilla_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail,  name='post_detail')
]