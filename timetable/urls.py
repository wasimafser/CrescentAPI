from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^first/$', views.first_page_view, name='first_page'),
    url(r'^test/$',views.testview, name='testpage')
]