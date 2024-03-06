## Steps of using the application

Requirements are saved and can be installed by:
pip install requirements.txt

In the VS code terminal, go to project folder where the manage.py is, e.g.:
C:\\django_new\\django_movielens\\projectmovies

First: _Delete the migrations and the database, created a command for this one:_

1. python manage.py delete_migrations_and_database
2. python manage.py makemigrations
3. python manage.py migrate
4. python manage.py import_movies
5. python manage.py runserver
6. python manage.py createsuperuser
7. python manage.py changepassword username3

## Open POSTMAN

Link: <http://127.0.0.1:8000/api/movies/>

### GET

![django-postman-GET](https://github.com/pkondacs/django_movielens/assets/57910212/ebf410cf-131f-4555-937d-a0071b804f8b)

### POST

Link: <http://127.0.0.1:8000/api/movies/>

{

&nbsp;   "title": "New movie xyz added",

&nbsp;   "genres": "Romance, Thriller added"

}

movieId is an Autofield so it gets automatically created

![django-postman-POST](https://github.com/pkondacs/django_movielens/assets/57910212/5bfc260c-be75-4122-9b43-746884225e2b)

### PUT

An example:

Link: <http://127.0.0.1:8000/api/movies/1/>

{

&nbsp;   "title": "Title has changed",

&nbsp;   "genres": "Genre has changed"

}

![django-postman-PUT](https://github.com/pkondacs/django_movielens/assets/57910212/616807e5-ae46-4208-9e66-3c99361c458a)

### PATCH

An example:

Link: <http://127.0.0.1:8000/api/movies/1/>

{

&nbsp;   "genres": "Genre has changed again"

}

![django-postman-PATCH](https://github.com/pkondacs/django_movielens/assets/57910212/2d991b15-ac1d-4848-a310-de723c105887)

## Rating a movie as a user

**Creating passwords for users:**

python manage.py changepassword username3

password (e.g.): movielens3

Open POSTMAN: <http://127.0.0.1:8000/api-token-auth/>

Change to POST

Body:

{

"username": "user3username",

"password": "user3password"

}

![django-postman-USER-AUTH](https://github.com/pkondacs/django_movielens/assets/57910212/0b598abe-39e7-485e-8a18-200239ab137f)

HTTP link include the following:

<http://127.0.0.1:8000/api/movies/1/rate_movie/>
