"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from argparse import Namespace
from django.contrib import admin
from django.urls import path, include
from products.views import Contact_us,contact_us_response,home_page,our_team,project,who_we_are




app_name = 'url'

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    # path('products/',include('products.urls')),
    path('home-page/',home_page,name='home_page'),
    path('projects/', project,name='project'),
    path('our-team/', our_team,name="our_team"),
    path('who-we-are', who_we_are,name='who_we_are'),
    path('contact-us/',Contact_us,name='contact_us'),
    path('response/',contact_us_response,name='contact_us_response')
]
