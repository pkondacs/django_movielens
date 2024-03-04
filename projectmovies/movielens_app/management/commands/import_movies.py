import pandas as pd
import pytz
from django.core.management.base import BaseCommand
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from movielens_app.models import Profile, Movie, GenomeScores, Tags, Ratings, Links

class Command(BaseCommand):
    help = 'Load a list of movies and genome scores from CSV files into the database'

    def handle(self, *args, **options):

        # Load movies data
        movies_csv_path = 'C:/Users/peter/Downloads/ml-20m/movies-smallset.csv'
        self.stdout.write(f'Loading movies data from {movies_csv_path}')
        movies_df = pd.read_csv(movies_csv_path)

        movie_objects = [
            Movie(
                movieId=row['movieId'],
                title=row['title'],
                genres=row['genres']
            )
            for index, row in movies_df.iterrows()
        ]
        Movie.objects.bulk_create(movie_objects)
        self.stdout.write(self.style.SUCCESS('Successfully loaded movies data.'))

        # Load profiles data
        profiles_csv_path = 'C:/Users/peter/Downloads/ml-20m/profiles-smallset.csv'
        self.stdout.write(f'Loading profiles data from {profiles_csv_path}')
        profiles_df = pd.read_csv(profiles_csv_path)

        for index, row in profiles_df.iterrows():
            # Create a User instance
            # Assuming that 'username' and 'email' are unique and not blank in your CSV.
            # You might need to add more logic here if that's not the case.
            user, created = User.objects.get_or_create(
                username=row['username'],
                defaults={'email': row['email']}  # Add other user fields if necessary
            )
            
            # Now create a Profile instance linked to the User instance
            # If a User was just created, it will also create a Profile.
            # If a User was retrieved, it will update the existing Profile.
            profile, created = Profile.objects.update_or_create(
                user=user,
                defaults={
                    'name': row['name'],
                    'location': row['location'],
                    # ... add other fields from the CSV if necessary
                    'created': datetime.datetime.fromtimestamp(row['timestamp'], tz=pytz.utc)
                }
            )
        self.stdout.write(self.style.SUCCESS('Successfully loaded profiles data.'))

        # Load tags data
        tags_csv_path = 'C:/Users/peter/Downloads/ml-20m/tags-smallset.csv'
        self.stdout.write(f'Loading tags data from {tags_csv_path}')
        tags_df = pd.read_csv(tags_csv_path)

        # Prepare a list of Tags objects with converted timestamps
        tags_objects = [
            Tags(
                userId=row['userId'],
                movie_id=row['movieId'],
                tag=row['tag'],
                # Convert epoch to timezone-aware datetime object
                timestamp=datetime.datetime.fromtimestamp(row['timestamp'], tz=pytz.utc)
            )
            for index, row in tags_df.iterrows()
        ]
        # Bulk create Tags objects
        Tags.objects.bulk_create(tags_objects)
        self.stdout.write(self.style.SUCCESS('Successfully loaded tags data.'))

        # Load ratings data
        ratings_csv_path = 'C:/Users/peter/Downloads/ml-20m/ratings-smallset.csv'
        self.stdout.write(f'Loading ratings data from {ratings_csv_path}')
        ratings_df = pd.read_csv(ratings_csv_path)

        ratings_objects = []
        for index, row in ratings_df.iterrows():
            # Retrieve the corresponding Profile/Movie instance
            # You need to ensure that the Profile/Movie instances have already been imported as per your previous step
            profile_instance = Profile.objects.get(id=row['userId'])
            movie_instance = Movie.objects.get(id=row['movieId'])
            
            # Now create a Ratings instance using the Profile instance
            rating = Ratings(
                userId=profile_instance,
                movieId=movie_instance,
                rating=row['rating'],
                timestamp=datetime.datetime.fromtimestamp(row['timestamp'], tz=pytz.utc)
            )
            ratings_objects.append(rating)

        # Bulk create Ratings objects
        Ratings.objects.bulk_create(ratings_objects)
        self.stdout.write(self.style.SUCCESS('Successfully loaded ratings data.'))

        # Load links data
        links_csv_path = 'C:/Users/peter/Downloads/ml-20m/links.csv'
        self.stdout.write(f'Loading links data from {links_csv_path}')
        links_df = pd.read_csv(links_csv_path)
        # Convert NaN to None for tmdbId
        links_df = pd.read_csv(links_csv_path, dtype={'tmdbId': pd.Int64Dtype()})

        # Iterate over the DataFrame and create Links objects
        links_objects = []
        for index, row in links_df.iterrows():
            link_obj = Links(
                movieId=int(row['movieId']),
                imdbId=int(row['imdbId']),
                tmdbId=row['tmdbId'] if pd.notnull(row['tmdbId']) else None
            )
            links_objects.append(link_obj)
            
        Links.objects.bulk_create(links_objects)
        self.stdout.write(self.style.SUCCESS('Successfully loaded links data.'))

    
        # Load genome scores data
        genome_scores_csv_path = 'C:/Users/peter/Downloads/ml-20m/genome-scores-smallset.csv'
        self.stdout.write(f'Loading genome scores data from {genome_scores_csv_path}')
        genome_scores_df = pd.read_csv(genome_scores_csv_path)

        genome_score_objects = [
            GenomeScores(
                movieId=row['movieId'],
                tagId=row['tagId'],
                relevance=row['relevance']
            )
            for index, row in genome_scores_df.iterrows()
        ]
        GenomeScores.objects.bulk_create(genome_score_objects)
        self.stdout.write(self.style.SUCCESS('Successfully loaded genome scores data.'))