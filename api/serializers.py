from rest_framework_json_api import serializers

from .models import Author, Book, Genre, BookInstance, BorrowHeader, BorrowDetail, Customer
from .utils import (
    ResourceRelatedGenreField, ResourceRelatedAuthorField
)

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    genre = ResourceRelatedGenreField(queryset=Genre.objects, many=True)
    author = ResourceRelatedAuthorField(queryset=Author.objects, many=True)

    class Meta:
        model = Book
        fields = ('name', 'isbn', 'summary', 'author', 'genre')

class InstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstance
        fields = ('book', 'status')

class BorrowDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowDetail
        fields = '__all__'

class BorrowHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowHeader
        fields = '__all__'

class NestedBorrowHeaderSerializer(serializers.ModelSerializer):
    BorrowDetailHeader = BorrowDetailSerializer(many=True)

    class Meta:
        model = BorrowHeader
        fields = ['header_id', 'customer_id', 'start_date', 'end_date', 'total', 'created_date', 'BorrowDetailHeader']