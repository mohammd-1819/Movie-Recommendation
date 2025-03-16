from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView
from ..models import ActorAndDirector
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from ..serializers import ActorAndDirectorSerializer
from ..utility.pagination import Pagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


@extend_schema(
    tags=['Actor And Directors'],
    summary='List of all actor and directors',
    responses={200: ActorAndDirectorSerializer(many=True)},
    auth=[]

)
class ActorAndDirectorsListView(ListAPIView):
    queryset = ActorAndDirector.objects.all()
    serializer_class = ActorAndDirectorSerializer
    pagination_class = Pagination


