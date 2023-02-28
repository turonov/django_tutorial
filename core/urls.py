

from django.urls import path
from django.http import HttpResponse,HttpRequest,JsonResponse
def index(request:HttpRequest):
    
    return HttpResponse("<h1>Home page</h1>")

urlpatterns = [
    path('', index),
]
