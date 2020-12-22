from django.shortcuts import render
from django.http import HttpResponse
from realtors.models import Realtor
from listings.models import Listing

from listings.choices import price_choices, bedroom_choices, state_choices
# Create your views here.
# def index(request):
#     return HttpResponse('<h1>Gloria</h1>')

def about(request):
    realtors = Realtor.objects.all()
    context = {'realtors': realtors}
    return render(request, 'real_estate_pages/about.html', context)

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)[:3]
    context = {
        'listings':listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        
    }

    return render(request, 'real_estate_pages/index.html', context)