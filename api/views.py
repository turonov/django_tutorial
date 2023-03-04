from django.http import HttpResponse,HttpRequest,JsonResponse
import json
from .models import Person



def index(request:HttpRequest):
    person = Person.objects.all()
    print(person[0])
    return JsonResponse({})

def get_data(request:HttpRequest):

    if request.method == "POST":
        data = request.body.decode()
        print(json.loads(data))

    if request.method =="GET":
        print('GET')

    return HttpResponse("hello world")
