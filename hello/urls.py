from django.urls import path
from . import views 
urlpatterns = [
    path("", views.index, name="index"),
    path("Long", views.Long, name="Long "),
    path("Nhan", views.Nhan, name="Nhan"),
    path("<str:name>", views.greet, name="greet")
]