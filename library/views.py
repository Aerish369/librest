from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from .filters import BookFilter
from .models import Book
from .serializers import BookSerializer



class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    search_fields = ['title', 'description', 'author__full_name']
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = BookFilter
