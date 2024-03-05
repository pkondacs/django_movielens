from rest_framework import serializers
from movielens_app.models import Movie, Ratings, Tags

# Using this as our main serializer class 
class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.CharField()  # Change this to a CharField to accept input
    tags = serializers.SerializerMethodField()

    def get_genres(self, instance):
        return instance.genres.split("|") if instance.genres else []

    def get_tags(self, instance: Movie):
        # Get all tags related to the movie
        tags = instance.tags.all()
        return ", ".join(tag.tag for tag in tags)
    
    def create(self, validated_data):
        genres_data = validated_data.pop('genres', '')
        movie = Movie.objects.create(**validated_data)
        movie.genres = genres_data  # Assuming genres is a CharField in your model
        movie.save()
        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)  # Update title
        instance.genres = validated_data.get('genres', instance.genres)  # Update genres
        instance.save()
        return instance

    class Meta:
        model = Movie
        fields = ['movieId', 'title', 'genres', 'tags']

class SubmitRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ["rating"]

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ["userId", "movieId", "rating", "timestamp"]

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ["userId", "movie", "tag", "timestamp"]
