from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	path('author/', views.AuthorList.as_view(), name='authorlist'),
	path('author/<int:pk>/', views.AuthorDetail.as_view(), name='authordetail'),
	path('customer/', views.CustomerList.as_view(), name='customerlist'),
	path('customer/<int:pk>/', views.CustomerDetail.as_view(), name='customerdetail'),
	path('books/', views.BookList.as_view(), name='booklist'),
	path('books/<int:pk>/', views.BookDetail.as_view(), name='bookdetail'),
	path('borrow/', views.Borrowheader.as_view(), name='borrowheader'),
	path('borrow/<int:pk>/', views.NestedBorrowDetail.as_view(), name='borrowdetail'),
]