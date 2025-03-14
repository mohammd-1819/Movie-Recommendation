from rest_framework import serializers
from movie.models import ActorAndDirector


class ActorAndDirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActorAndDirector
        exclude = ('id',)
