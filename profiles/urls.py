from django.conf.urls import url, include
from . import api, views

urlpatterns = [
    url(r'^login', views.login_view, name='login')
]