from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.BookList.as_view(), name='home'),
    path('book/<int:id>/', views.book_detail, name='book-detail'),
]