from django.urls import path
from . import views

urlpatterns = [
    path('food/', views.TvShowView.as_view(), name='food'),
]
