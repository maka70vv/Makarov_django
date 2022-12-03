from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, FormView
from . import parser, models, forms
# Create your views here.
class ParserView(ListView):
    model = models.Laptops
    template_name = 'laptops_list.html'

    def get_queryset(self):
        return models.Laptops.objects.all()

class ParserFormView(FormView):
    template_name = 'parser_laptops.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('<h1>Данные успешно получены.......</h1>')
        else:
            return super(ParserFormView, self).post(request, *args, **kwargs)