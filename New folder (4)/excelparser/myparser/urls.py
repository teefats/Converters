from django.urls import path
from . import views

urlpatterns = [
    path('myparser/', views.home, name='home')
]
