from rest_framework import serializers
from movie.models import Series, Season, Episode
from django.utils.timezone import now


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        exclude = ('id',)

    def validate_seasons_count(self, value):
        if value < 1:
            raise serializers.ValidationError("season count must be at least 1")
        return value

    def validate_episodes_count(self, value):
        if value < 1:
            raise serializers.ValidationError("episode count must be at least 1")
        return value


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        exclude = ('id',)

    def validate_number(self, value):
        if value < 1:
            raise serializers.ValidationError("season number must be at least 1")
        return value

    def validate_episodes_count(self, value):
        if value < 1:
            raise serializers.ValidationError("episode count must be at least 1")
        return value

    def validate(self, data):
        series = data.get('series')
        number = data.get('number')

        # check if there is a duplicated number for a season
        if Season.objects.filter(series=series, number=number).exists():
            raise serializers.ValidationError("season already exists")

        return data


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        exclude = ('id',)

    def validate_number(self, value):
        if value < 1:
            raise serializers.ValidationError("episode number must be at least 1")
        return value

    def validate_duration(self, value):
        if value < 1:
            raise serializers.ValidationError("duration must be above 1 minute")
        return value

    def validate_release_date(self, value):
        if value > now().date():
            raise serializers.ValidationError("invalid release date")
        return value

    def validate(self, data):
        season = data.get('season')
        number = data.get('number')

        # check if there is a duplicated number for an episode
        if Episode.objects.filter(season=season, number=number).exists():
            raise serializers.ValidationError("episode already exists")

        return data
