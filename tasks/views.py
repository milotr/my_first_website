from django.shortcuts import render
tasks = ["foo", "bar", "baz"]
# Create your views here.
# These function will request the HTML pages. 
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
        
    })

def add(request):
    return render(request, "tasks/add.html")