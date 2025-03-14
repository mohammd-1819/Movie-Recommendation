from rest_framework import serializers
from movie.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        exclude = ('id',)
        read_only_fields = ('created_at', 'updated_at')
