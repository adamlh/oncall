
from django.urls import include, path
from .views import SpmView

urlpatterns = [
    path('', SpmView.as_view(), name='SpmView'),
]
