from django.conf.urls import urls, path
from . import views

urlpatterns = [
    path('search/$', views.search, name='search'),
]