from rest_framework import serializers
from movie.models import Content


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        exclude = ('id',)
        read_only_fields = ('created_at', 'updated_at')
