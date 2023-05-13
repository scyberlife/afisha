from django.urls import path
from .views import (DirectorView, SingleDirectorView, DirectorCreateView, DirectorUpdateView,
    MoviesView, SingleMovieView, MovieCreateView, MovieUpdateView,
    ReviewsView, SingleReviewView, ReviewCreateView, ReviewUpdateView, MoviesReviewsView,)

urlpatterns = [
    path('api/v1/directors/', DirectorView.as_view()),
    path('api/v1/directors/<int:id>/', DirectorView.as_view()),
    path('api/v1/directors/create/', DirectorCreateView.as_view()),
    path('api/v1/directors/<int:pk>/update/', DirectorUpdateView.as_view()),
    path('api/v1/directors/<int:pk>/delete/', DirectorUpdateView.as_view()),
    path('api/v1/movies/', MoviesView.as_view()),
    path('api/v1/movies/<int:id>/', DirectorView.as_view()),
    path('api/v1/movies/<int:pk>/update/', MovieUpdateView.as_view()),
    path('api/v1/movies/<int:pk>/delete/', MovieUpdateView.as_view()),
    path('api/v1/movies/create/',  MovieCreateView.as_view()),
    path('api/v1/reviews/', ReviewsView.as_view()),
    path('api/v1/reviews/<int:id>/', ReviewsView.as_view()),
    path('api/v1/movies/reviews/', MoviesReviewsView.as_view()),
    path('api/v1/movies/reviews/create/', ReviewCreateView.as_view()),
    path('api/v1/movies/reviews/<int:pk>/update/', ReviewUpdateView.as_view()),
    path('api/v1/movies/reviews/<int:pk>/delete/', ReviewUpdateView.as_view()),
]