from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
# router.register(r'ratings', RatingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # ... other url patterns ...
]

urlpatterns += router.urls

# urlpatterns = [
#     # path('movies/', MovieListCreateAPIView.as_view(), name='movie-list-create'),
#     # path('movies/<int:movieId>/', MovieDetailAPIView.as_view(), name='movie-detail'),
#     path('movies/<int:movieId>/rate/', RateMovieAPIView.as_view(), name='movie-rate'),
#     path('movies/', views.movie_list_create, name='movie-list-create')
# ]
