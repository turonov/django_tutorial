from django.http import HttpResponse,HttpRequest,JsonResponse
import json
def index(request:HttpRequest):
    data=request.GET
    a = int(data.get('a',0))
    b = int(data.get('b',0))
    return JsonResponse({'sum':a+b})

def get_data(request:HttpRequest):

    if request.method == "POST":
        data = request.body.decode()
        print(json.loads(data))

    if request.method =="GET":
        print('GET')

    return JsonResponse("hello world")
