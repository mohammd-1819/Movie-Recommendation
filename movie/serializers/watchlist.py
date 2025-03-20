from rest_framework import serializers
from movie.models import Watchlist


class WatchlistSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Watchlist
        exclude = ('id',)

    def validate(self, data):
        user = self.context['request'].user
        content = data.get('content')

        if Watchlist.objects.filter(user=user, content=content).exists():
            raise serializers.ValidationError("This content is already in your watchlist.")

        return data
