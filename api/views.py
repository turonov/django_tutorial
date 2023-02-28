from django.http import HttpResponse,HttpRequest,JsonResponse

def index(request:HttpRequest):
    data=request.GET
    a = int(data.get('a',0))
    b = int(data.get('b',0))
    return JsonResponse({'sum':a+b})
