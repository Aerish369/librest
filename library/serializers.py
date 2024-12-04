from rest_framework import serializers
from .models import Book, Author, Tag, Profile

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['full_name', 'bio']

class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    tag = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True) 
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'author', 'published_date', 'tag']


class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    class Meta:
        model = Profile
        fields = ['id', 'bio', 'user_id', 'birth_date', 'created_at']