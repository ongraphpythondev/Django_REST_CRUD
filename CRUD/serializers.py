from rest_framework import serializers
from CRUD.models import Book

class Book_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'author' , 'created_at')