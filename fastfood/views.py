from django.shortcuts import render
from . import models
from . import forms
from django.http import HttpResponse
from django.views import generic
# Create your views here.
def order_view(request):
    order = models.Order.objects.all()
    return render(request, 'fastfood.html', {'order':order})

def add_food_view(request):
    method = request.method
    if method == 'POST':
        form = forms.FastFoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return  HttpResponse('<center></center>')

#GET
class TvShowView(generic.ListView):
    template_name = 'fastfood.html'
    queryset = models.Order.objects.all

    def get_queryset(self):
        return models.Order.objects.all()