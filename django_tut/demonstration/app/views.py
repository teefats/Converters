# views.py 
from django.shortcuts import render, HttpResponse
import requests

# Create your views here. 
def index(request):
    return HttpResponse('Hello World!')

def test(request):
    return HttpResponse('My second view!')
