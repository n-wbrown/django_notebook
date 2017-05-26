"""dja_0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

#from django.contrib.auth import views as auth_views
import django.contrib.auth

#admin MUST come last otherwise its urls take precedecs over accounts
urlpatterns = [
    url(r'^st/', include('st_0.urls')),
    #url(r'^', include('st_0.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),    
    url(r'^admin/', admin.site.urls),
]


#Add URL maps to redirect the base URL to our application
#The permanent flag sets error code to 301, 302, false (302) by defautle
# ^ not important
from django.views.generic import RedirectView
urlpatterns += [
    url(r'^$', RedirectView.as_view(url='/st/', permanent=True)),
]
