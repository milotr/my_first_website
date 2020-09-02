from django.urls import path
from . import views

# this is linking to views of the application
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add" )
]