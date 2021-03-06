"""CrescentAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^login$', auth_views.LoginView.as_view()),
    url(r'^home/$', views.home_view, name='home'),
    url(r'^', include('timetable.urls')),
    url(r'^', include('profiles.urls')),
    url(r'^exam/', include('exam.urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Admin Site Config
admin.sites.AdminSite.site_header = 'Crescent API'
admin.sites.AdminSite.site_title = 'Crescent API'
admin.sites.AdminSite.index_title = 'Crescent API'
