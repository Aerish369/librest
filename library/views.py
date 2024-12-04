from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet


from .filters import BookFilter
from .models import Book, Profile
from .serializers import BookSerializer, ProfileSerializer



class BookViewSet(ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer
    search_fields = ['title', 'author__full_name', 'tag__tag']
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = BookFilter


class ProfileViewSet(CreateModelMixin,
                     RetrieveModelMixin,
                     UpdateModelMixin, 
                     GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

#! Make Profile API as it is not included in the DJOSER by default 
#! Then Only proceed developing further. 