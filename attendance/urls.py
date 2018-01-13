from django.conf.urls import url
from django.conf.urls import include

from . import views

urlpatterns = [
    url(r'^reportall/$', views.index, name='index'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]