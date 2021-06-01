"""oncall URL Configuration

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
from django.urls import path,include
from django.conf.urls.static import static
from rota.views import  RotaView, RotaTotalView, search
from engineering.views import EngView
from laboratory.views import LabView
from spm.views import SpmView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('total/', RotaTotalView.as_view(), name='RotaTotalView'),
    path('eng/', EngView.as_view(), name='EngView'),
    path('lab/', LabView.as_view(), name='LabView'),
    path('spm/', SpmView.as_view(), name='SpmView'),
    path('', RotaView.as_view(), name='RotaView'),
    path('search/$', search, name='search'),
  
]
