# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager, User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True,blank=True, db_column='userId') # creating one to one relationship with User default model of django
    name = models.CharField(max_length=200,blank=True,null=True)
    username = models.CharField(max_length=200,blank=True,null=True)
    location = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(max_length=500,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True, db_column='timestamp') # auto_now_add adds timestamp automatically as model instance is created
    def __str__(self):
        return str(self.username)

class Movie(models.Model):
    movieId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    def __str__(self):
        return str(self.movieId)  # Use an existing field

class Ratings(models.Model):
    userId = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='ratings', db_column='userId')
    movieId = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings', db_column='movieId')
    rating = models.FloatField()
    timestamp = models.DateTimeField()
    def __str__(self):
        return str(self.movieId)  # Use an existing field

class Tags(models.Model):
    userId = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='tags', db_column='movieId') # telling django that there is a relationship between the two models
    tag = models.CharField(max_length=255)
    timestamp = models.DateTimeField()

    def __str__(self):
        return str(self.userId)  # Use an existing field
        
class GenomeScores(models.Model):
    movieId = models.IntegerField()
    tagId = models.IntegerField()
    relevance = models.FloatField()
    def __str__(self):
        return str(self.tagId)  # Use an existing field
   
class Links(models.Model):
    movieId = models.IntegerField()
    imdbId = models.IntegerField()
    tmdbId = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.movieId)  # Use an existing field
