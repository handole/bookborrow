# Borrowing Books
### Django-Restfull
Create virtualenv in your base folder apps, install package pip in requirements using python 3 above

On your folder apps, in your terminal command with
`> pip install -r requirements.txt`

after installed the library, migration database. using postgres, so create database with name librarydb
then migration the database
`> python manage.py makemigrations`

`> python manage.py migrations`

createsuperuser, fill anything username, email and password
`> python manage.py createsuperuser`

running this aplication
`> python manage.py runserver`

open browser, with address localhost:8000/admin/ this for superuser

with postman, endpoint
`localhost:8000/author/` method get or post

`localhost:8000/author/<id>/` method get, put or delete

`localhost:8000/customer/` method get or post

`localhost:8000/customer/<id>/` method get, put or delete

`localhost:8000/books/` method get or post

`localhost:8000/books/<id>/` method get, put or delete

`localhost:8000/borrow/` method get or post

`localhost:8000/borrow/<id>/` method get, put or delete