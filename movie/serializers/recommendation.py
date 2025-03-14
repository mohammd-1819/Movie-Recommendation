from rest_framework import serializers
from movie.models import Recommendation


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        exclude = ('id',)
