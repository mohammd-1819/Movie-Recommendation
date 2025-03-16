from django.db import models


class ActorAndDirector(models.Model):
    ROLE_CHOICES = [
        ('actor', 'Actor'),
        ('director', 'Director')
    ]

    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    photo = models.FileField(upload_to='img/actor_and_directors', blank=True, null=True)

    def __str__(self):
        return self.name
