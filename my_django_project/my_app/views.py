from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import View


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

books_content = [
    {
        "id": 1,
        "book": "book_1",
        "title": "title_1",
        "author": "author_1"
    },
    {
        "id": "2",
        "book": "book_2",
        "title": "title_2",
        "author": "author_2"
    }
]

def validate(book_data):
    return True

# Function based views
@csrf_exempt
def list_books(request: HttpRequest,**kwargs: dict):
    if request.method == 'GET':
        return HttpResponse(books_content)
    elif request.method == 'POST':
        book_data = request.POST
        if not validate(book_data):
            return HttpResponse(f"The POST data {book_data} is invalid")
        book = book_data.get('book')
        title = book_data.get('title')
        author = book_data.get('author')
        append_data = {
            'book': book,
            'title': title,
            'author': author
        }
        books_content.append(append_data)
        return HttpResponse(books_content)
    elif request.method == 'DELETE':
        return HttpResponseNotFound(f"Type {request.method} is not supported")

# The dispatch method of method_decorator is checking the request method whethrt the method is GET, POST etc..
@method_decorator(csrf_exempt, name = 'dispatch')
class ListBooks(View):
   def get(self, request: HttpRequest, **kwargs: dict):
       return HttpResponse(books_content)
   
   def post(self, request: HttpRequest, **kwargs: dict):
       book_data = request.POST
       if not validate(book_data):
           return HttpResponseBadRequest(f"The post data is invalid")
       book = book_data.get('book')
       title = book_data.get('title')
       author = book_data.get('author')
       append_data = {
           "book": book,
           "title": title,
           "author": author
       }
       books_content.append(append_data)
       return HttpResponse(books_content)
       
# Html based views 
def my_view(request: HttpRequest):
    #Prepare q webpage(html) with dynamic content
    html_content = "<html><body>"
    for content in books_content:
        html_content += "<p>"+str(content)+"</p>"
    html_content+="</body></html>"
    return HttpResponse(html_content)