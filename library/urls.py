from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.BookList.as_view(), name='home'),
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
]