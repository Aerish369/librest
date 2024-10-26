from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer

@api_view()
def books(request):
    queryset = ( Book.objects
        .select_related('author')
        .prefetch_related('author','tag')
        .all())
    serializer = BookSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def book_detail(request, id):
    book = Book.objects.get(pk=id)
    serializer = BookSerializer(book)
    return Response(serializer.data)
    