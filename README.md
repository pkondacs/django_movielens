## Steps of using the application

In the VS code terminal, go to project folder where the manage.py is, e.g.:

C:\\django_new\\django_movielens\\projectmovies

_Delete the migrations and the database, created a command for this one:_

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

<https://drive.google.com/file/d/1OV2TREfnksCgMbfjwL5jmME8-mKxdd_n/view?usp=sharing>

### PUT

An example:

Link: <http://127.0.0.1:8000/api/movies/1/>

{

&nbsp;   "title": "Title has changed",

&nbsp;   "genres": "Genre has changed"

}

<https://drive.google.com/file/d/1KFrjOOPbmF_m4vyExOH8Sly0qjv-43y3/view?usp=sharing>

### PATCH

An example:

Link: <http://127.0.0.1:8000/api/movies/1/>

{

&nbsp;   "genres": "Genre has changed again"

}

<https://drive.google.com/file/d/1-AXx7vk4YnL8CTbTu3PJUdmcT681awyF/view?usp=sharing>

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

<https://drive.google.com/file/d/1nGi2mxIS_4zCWD2xGWB2rUJbP-iNzIoy/view?usp=sharing>

HTTP link include the following:

<http://127.0.0.1:8000/api/movies/1/rate_movie/>
