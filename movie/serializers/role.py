from rest_framework import serializers
from movie.models import Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        exclude = ('id',)
