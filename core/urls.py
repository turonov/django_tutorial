

from django.urls import path
from django.http import HttpResponse,HttpRequest,JsonResponse
def index(request:HttpRequest):
    
    return JsonResponse({
        'result':True
    })

urlpatterns = [
    path('', index),
]
