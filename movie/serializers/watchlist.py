from rest_framework import serializers
from movie.models import Watchlist


class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        exclude = ('id',)

    def validate(self, data):
        user = data.get('user')
        content = data.get('content')

        if Watchlist.objects.filter(user=user, content=content).exists():
            raise serializers.ValidationError("this content is already in your watchlist")

        return data
