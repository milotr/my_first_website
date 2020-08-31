from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#request HTML server
def index(request):
    return render(request, "hello/index.html")

def Long(resquest):
    return HttpResponse("Hello, sir. Welcome to your first website!")

def Nhan(request):
    return HttpResponse("Accessing your girlfriend's love...")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
