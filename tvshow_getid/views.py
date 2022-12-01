from django.shortcuts import get_object_or_404
from . import models
from . import forms
from django.views import generic
# Create your views here.

#get id
class TvShowView(generic.ListView):
    template_name = 'tvshow.html'
    queryset = models.TvShow.objects.all()

    def get_queryset(self):
        return models.TvShow.objects.all()


class TvShowDetailView(generic.DetailView):
    template_name = 'films.html'

    def get_object(self, **kwargs):
        tvshow_id = self.kwargs.get('id')
        return get_object_or_404(models.TvShow, id=tvshow_id)

class TvShowCreateView(generic.CreateView):
    template_name = 'add_tv.html'
    form_class = forms.TvShow
    queryset = models.TvShow.objects.all()
    success_url = '/tvshow/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(TvShowCreateView, self).form_valid(form=form)



#update TvShow

class TvShowUpdateView(generic.UpdateView):
    template_name = 'update_tv.html'
    form_class = forms.TvShow
    success_url = '/tvshow/'

    def get_object(self, **kwargs):
        tvshow_id = self.kwargs.get('id')
        return get_object_or_404(models.TvShow, id=tvshow_id)

    def form_valid(self, form):
        return super(TvShowUpdateView, self).form_valid(form=form)



#delete TvShow
class TvShowDeleteView(generic.DeleteView):
    template_name = 'tvdelete.html'
    success_url = '/tvshow/'

    def get_object(self, **kwargs):
        tvshow_id = self.kwargs.get('id')
        return get_object_or_404(models.TvShow, id=tvshow_id)