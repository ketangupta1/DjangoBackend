from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def dummy_view(request):
    return HttpResponse("Hello World")

def dummy_view_num(request, view_num):
    return HttpResponse(f"Hello world {view_num}")

@csrf_exempt
def dummy_view_kwargs(request:HttpRequest, num, **kwargs):
    # print(request.method)
    if request.method == 'GET':
        print(f"Get view {request.GET} ")
        # You can see the print statement if you made GET request via query parameter: http://localhost:8000/my_app/view_kwargs_68?name=Ketan
    elif request.method == 'POST':
        print(f"Post View {request.POST}")
    return HttpResponse(f"Hello World {num} and {kwargs}")