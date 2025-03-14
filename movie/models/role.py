from django.db import models
from .actor_and_director import ActorAndDirector
from .content import Content


class Role(models.Model):
    person = models.ForeignKey(ActorAndDirector, on_delete=models.CASCADE, related_name='role')
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    character_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.person.name} as {self.character_name} in {self.content.title}"
