

from django.urls import path
from api.views import index
from api.views import get_data

urlpatterns = [
    path('', index),
    path('get_data/',get_data)
]
