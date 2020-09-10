from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# These function will request the HTML pages. 
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value= 1, max_value= 10)


def index(request):
    #creating sessions
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
        
    })

def add(request):
    #Client-Server validation:
    #if the user submit a form
    if request.method == "POST":
        #then get all the data into form
        form = NewTaskForm(request.POST)
        if form.is_valid():
            # if Form is valid, get cleaned data from "task" into variable 
            # task and add it into the tasks list.
            task = form.cleaned_data["task"]
            task.append(task)
            #?
            request.session["task"] += [task]
            #Redirect after added the new string to the list
            #reverse("tasks:index") is django will figure out the 
            #name "index" and return the html page
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html",{
        "form": NewTaskForm()
    })