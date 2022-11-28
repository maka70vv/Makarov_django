from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('book_posts/', views.book_post, name='book_post'),
    path('tvshow/', views.TvShowView.as_view(), name='tvshow'),
    path('tvshow_detail/<int:id>/', views.TvShowDetailView.as_view(), name='show_detail'),
]
