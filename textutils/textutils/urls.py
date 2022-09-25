"""textutils URL Configuration

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
from django.contrib import admin
from django.urls import path
# importing self made file Views.py
from . import Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Views.index,name='index'),
    path('analyze/',Views.analyze,name='analyze')
]    
    
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',Views.index,name='index'),
#   path('removepunc/',Views.removepunc,name='removepunc')
    # path('removepunc/',Views.removepuncuation,name='pucn'),
    # path('homepage/',Views.txtfile,name='txt'),
    # path('about/',Views.about,name='about'),
    # path('html/',Views.html,name='html'),
    # path('link/',Views.link,name='link'),
# ]