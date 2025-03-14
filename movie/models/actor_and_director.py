from django.db import models


class ActorAndDirector(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    photo = models.FileField(upload_to='img/actor_and_directors', blank=True, null=True)

    def __str__(self):
        return self.name
