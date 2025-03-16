from rest_framework import serializers
from movie.models import Content


class CreateContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        exclude = ('id', 'actors')
        read_only_fields = ('created_at', 'updated_at')
