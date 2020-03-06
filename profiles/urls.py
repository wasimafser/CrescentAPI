from django.conf.urls import url, include
from . import api, views

urlpatterns = [
    url(r'^login$', views.login_view, name='login'),
    url(r'^subjects/$', views.SubjectView.as_view(), name='subject_view'),
    # API
    url(r'^api/subject/$', api.SubjectAPI.as_view(), name='subject_api'),
]