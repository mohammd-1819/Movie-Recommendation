from django.db import models
from .actor_and_director import ActorAndDirector
from .genre import Genre
from django.db.models import Avg


class Content(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('movie', 'Movie'),
        ('series', 'Series'),
    ]

    title = models.CharField(max_length=200)
    original_title = models.CharField(max_length=200, blank=True, null=True)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPE_CHOICES)
    release_date = models.DateField()
    description = models.TextField()
    poster = models.ImageField(upload_to='img/posters', blank=True, null=True)
    genres = models.ManyToManyField(Genre, related_name='contents')
    director = models.ForeignKey(ActorAndDirector, on_delete=models.CASCADE, related_name='directed_contents')
    actors = models.ManyToManyField(ActorAndDirector, related_name='acted_in_contents', through='Role')
    duration = models.PositiveIntegerField(help_text="duration of the content")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def average_rating(self):
        return self.ratings.aggregate(Avg('rating'))['rating__avg'] or 0

    def __str__(self):
        return self.title

