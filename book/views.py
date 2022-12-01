from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from tvshow_getid import forms
from . import models
# Create your views here.
def hello(request):
    return HttpResponse('Hello World')

#Функция для отображения моделек
def book_post(request):
    book_post = models.Book.objects.all()
    return render(request, 'book.html', {'post_book':book_post})

