import datetime

from django.shortcuts import render

# Create your views here.
# The function will also include Python logic with HTML.
def index(request):
    now = datetime.datetime.now()
    return render(request, "NewYear/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })