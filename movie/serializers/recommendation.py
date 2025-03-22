from rest_framework import serializers
from movie.models import Recommendation
from ..serializers import ContentSerializer


class RecommendationSerializer(serializers.ModelSerializer):
    content = ContentSerializer()

    class Meta:
        model = Recommendation
        exclude = ('id',)
