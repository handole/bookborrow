from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Book, BookInstance, Author, Customer, BorrowHeader, BorrowDetail
from .serializers import BookSerializer, InstanceSerializer, AuthorSerializer, CustomerSerializer, BorrowHeaderSerializer, NestedBorrowHeaderSerializer

class AuthorList(APIView):
	def get(self, request, format=None):
		author = Author.objects.all()
		serializer = AuthorSerializer(author, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = AuthorSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

class AuthorDetail(APIView):
	def get_object(self, pk):
		try:
			return Author.objects.get(pk=pk)
		except Author.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		author = self.get_object(pk)
		serializer = AuthorSerializer(author)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		author = self.get_object(pk)
		serializer = AuthorSerializer(author, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)


class CustomerList(APIView):
	def get(self, request, format=None):
		customer = Customer.objects.all()
		serializer = CustomerSerializer(customer, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = CustomerSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

class CustomerDetail(APIView):
	def get_object(self, pk):
		try:
			return Customer.objects.get(pk=pk)
		except Customer.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		customer = self.get_object(pk)
		serializer = CustomerSerializer(customer)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		customer = self.get_object(pk)
		serializer = CustomerSerializer(Customer, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)


class BookList(APIView):
	def get(self, request, format=None):
		books = Book.objects.all()
		serializer = BookSerializer(books, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = BookSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

class BookDetail(APIView):
	def get_object(self, pk):
		try:
			return Book.objects.get(pk=pk)
		except Book.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		book = self.get_object(pk)
		serializer = BookSerializer(book)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		book = self.get_object(pk)
		serializer = BookSerializer(book, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		book = self.get_object(pk)
		book.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class Borrowheader(APIView):
	def get(self, request, format=None):
		borrowH = BorrowHeader.objects.all()
		serializer = NestedBorrowHeaderSerializer(borrowH, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = NestedBorrowHeaderSerializer(data=request.data)
		if serializer.is_valid():
			bh = serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NestedBorrowDetail(APIView):
	def get_object(self, pk):
		try:
			return BorrowHeader.objects.get(pk=pk)
		except BorrowHeader.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		borrowHeader = self.get_object(pk)
		serializer = NestedBorrowHeaderSerializer(borrowHeader)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		borrowHeader = self.get_object(pk)
		serializer = NestedBorrowHeaderSerializer(borrowHeader, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
