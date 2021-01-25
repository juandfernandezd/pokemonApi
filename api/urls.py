from django.urls import path
from api import views

# URL's for create and get dataset, get and filter rows
urlpatterns = [
    path('register/<int:id>/', views.register),
]