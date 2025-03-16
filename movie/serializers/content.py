from rest_framework import serializers
from movie.models import Content, ActorAndDirector, Genre


class ContentSerializer(serializers.ModelSerializer):
    actors = serializers.SlugRelatedField(slug_field='name', queryset=ActorAndDirector.objects.all(), many=True)
    genres = serializers.SlugRelatedField(slug_field='name', queryset=Genre.objects.all(), many=True)

    class Meta:
        model = Content
        exclude = ('id',)
        read_only_fields = ('created_at', 'updated_at')
