from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from . import models
# Create your views here.
def hello(request):
    return HttpResponse('Hello World')

#Функция для отображения моделек
def book_post(request):
    book_post = models.Book.objects.all()
    return render(request, 'book.html', {'post_book':book_post})

class TvShowView(generic.ListView):
    template_name = 'tvshow.html'
    queryset = models.TvShow.objects.all()

    def get_queryset(self):
        return models.TvShow.objects.all()


#get id
class TvShowDetailView(generic.DetailView):
    template_name = 'films.html'

    def get_object(self, **kwargs):
        tvshow_id = self.kwargs.get('id')
        return get_object_or_404(models.TvShow, id=tvshow_id)