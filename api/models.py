import uuid
from datetime import date

from django.db import models
from django.utils.translation import ugettext_lazy as _

from isbn_field import ISBNField
from django.contrib.auth.models import User

# Create your models here.
class TimeStampedMixin(models.Model):
    created_date = models.DateTimeField(editable=False, blank=True, null=True,
        auto_now_add=True, verbose_name=_('created date'))
    last_modified = models.DateTimeField(editable=False, blank=True, null=True,
        auto_now=True, verbose_name=_('last modified'),)

    class Meta:
        abstract = True


class CatalogueMixin(TimeStampedMixin):
    name = models.CharField(max_length=600, verbose_name='name')
    is_active = models.BooleanField(default=True, verbose_name='is active')
    was_deleted = models.BooleanField(default=False, verbose_name='was deleted')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Genre(CatalogueMixin):
    class Meta:
        verbose_name = _('genre')
        verbose_name_plural = _('genres')


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField()

    def __str__(self):
        return '{0} ({1})'.format(self.first_name, self.last_name)


class Author(TimeStampedMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField('Birth', null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = _('author')
        verbose_name_plural = _('authors')

    def __str__(self):
        return '{0} ({1})'.format(self.first_name, self.last_name)


class Book(CatalogueMixin):
    author = models.ManyToManyField(Author, related_name='books', related_query_name='book')
    summary = models.TextField(max_length=1000)
    isbn = models.CharField(max_length=15, unique=True, null=True, blank=True)

    # ManyToManyField used because genre can contain many books.
    # Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    genre = models.ManyToManyField(Genre, related_name='books', related_query_name='book')

    class Meta:
        verbose_name = _('book')
        verbose_name_plural = _('books')
    
    class JSONAPIMeta:
        resource_name = 'books'


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='books', related_query_name='book')

    LOAN_STATUS = (
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='a')

    class Meta:
        verbose_name = _('book instance')
        verbose_name_plural = _('book instances')

    def __str__(self):
        return '{0} ({1})'.format(self.id, self.book.title)

class BorrowHeader(models.Model):
    header_id = models.BigIntegerField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField()
    total = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return str(self.header_id)

class BorrowDetail(models.Model):
    detail_id = models.BigIntegerField(primary_key=True)
    price = models.IntegerField()
    qty = models.IntegerField()
    total = models.IntegerField()
    borrow_header = models.ForeignKey(BorrowHeader, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='header')
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='books_borrow')

    def __str__(self):
        return str(self.detail_id)

