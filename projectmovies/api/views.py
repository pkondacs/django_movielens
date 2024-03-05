from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from movielens_app.models import Movie, Ratings  # Assuming Ratings is the correct model name
from .serializers import MovieSerializer, RatingSerializer

class MoviePagination(PageNumberPagination):
    page_size = 10  # Set the number of movies per page

class MovieViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing movie instances.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MoviePagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [OrderingFilter]
    ordering_fields = ['title', 'ratings']  # Specify fields which you want to be able to order by
    ordering = ['title']  # Default ordering
    
    @action(detail=True, methods=['post'], permission_classes=[AllowAny])
    def rate_movie(self, request, pk=None):
        movie_id = pk  # 'pk' is taken from the URL
        
        # If you want to allow anonymous users to rate movies,
        # you'll need to handle the case when request.user is AnonymousUser.
        if request.user.is_authenticated:
            user = request.user
        else:
            # Handle anonymous users here. For instance:
            # user = None or provide a default user or create a new user.
            data = request.data
        
        try:
            # Ensure that the movie exists
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response({'error': 'Movie not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        # Check if the user has already rated this movie
        # You need to decide how to handle ratings for anonymous users.
        rating, created = Ratings.objects.get_or_create(user=user, movie=movie)
        
        # Update the rating
        rating_serializer = RatingSerializer(rating, data=data)
        if rating_serializer.is_valid():
            rating_serializer.save()
            return Response(rating_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(rating_serializer.errors, status=status.HTTP_400_BAD_REQUEST)