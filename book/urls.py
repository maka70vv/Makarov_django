from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('book_posts/', views.book_post, name='book_post'),

]
