from django.urls import path
from .views import *

urlpatterns = [
    path("", indexView, name="index"),
    path("edit/<int:pk>", editView, name="edit"),
    path("delete/<int:pk>", deleteView, name="delete"),
]
