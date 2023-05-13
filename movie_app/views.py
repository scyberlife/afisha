from django.db.models import Count
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer



class DirectorView(generics.ListAPIView):
    queryset = Director.objects.annotate(movies_count=Count('movies'))
    serializer_class = DirectorSerializer

class SingleDirectorView(generics.RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class MoviesView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SingleMovieView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewsView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class SingleReviewView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class MoviesReviewsView(generics.ListAPIView):
    queryset = Movie.objects.annotate(avg_rating=Avg('reviews__stars'))
    serializer_class = MovieSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['reviews_serializer'] = ReviewSerializer
        return context    

class DirectorCreateView(generics.CreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class MovieCreateView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer




       