from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


class BookList(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# @api_view(['GET', 'POST'])
# def books(request):
#     if request.method == 'GET':
#         queryset = ( 
#             Book.objects
#             .select_related('author')
#             .prefetch_related('author','tag')
#             .all()
#             )
#         serializer = BookSerializer(queryset, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(0)
#         return Response('Okay')
    


@api_view()
def book_detail(request, id):
    book = Book.objects.get(pk=id)
    serializer = BookSerializer(book)
    return Response(serializer.data)
    