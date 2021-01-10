from django.shortcuts import render
from .thebooks import book_list
from .models import Books
from django.http import HttpResponse
from .trialparse import state_choices
from .booky import booky
# Create your views here.
# def home(request):
#     books =  Books.objects.all()
#     book_names = list()
#     book_items = book_list
#     for book in books:
#         book_names.append(book.title)
#     # return render(request, 'myparser/index.html', books)
#     response_html ='<br>'.join(book_names)
#     return HttpResponse(response_html)

def home(request):
    books =  Books.objects.all()
    context ={'books': books, 'state_choices':state_choices, 'booky':booky}

    # book_names = list()
    # book_items = book_list
    # for book in books:
    #     book_names.append(book.title)
    # return render(request, 'myparser/index.html', books)
    # response_html ='<br>'.join(book_names)
    return render(request, 'myparser/index.html', context)