from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def index(request):
#     return HttpResponse('<h1>Gloria</h1>')

def about(request):
    return render(request, 'real_estate_pages/about.html')

def index(request):
    return render(request, 'real_estate_pages/index.html')