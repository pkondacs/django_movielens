# Register your models here.
from django.contrib import admin
from .models import Movie, GenomeScores, Ratings, Tags, Links, Profile

admin.site.register(Movie)
admin.site.register(GenomeScores)
admin.site.register(Ratings)
admin.site.register(Tags)
admin.site.register(Links)
admin.site.register(Profile)