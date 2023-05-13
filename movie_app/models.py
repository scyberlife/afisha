from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator




class Director(models.Model):
    name = models.CharField(max_length=20)

class Genre(models.Model):
    name = models.CharField(max_length=255)

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    duration = models.TextField()
    director = models.ForeignKey('Director', on_delete=models.CASCADE, related_name='movies')
    genres = models.ManyToManyField(Genre, related_name='movies')


class Review(models.Model):
    text = models.CharField(max_length=255)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])

