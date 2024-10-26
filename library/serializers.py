from rest_framework import serializers
from .models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['full_name', 'bio']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    tag = serializers.StringRelatedField(many=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'author', 'published_date', 'tag']
