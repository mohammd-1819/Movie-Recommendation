from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView
from ..models import Series, Season, Episode
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from ..serializers import SeriesSerializer, SeasonSerializer, EpisodeSerializer
from ..utility.pagination import Pagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


@extend_schema(
    tags=['Series'],
    summary='List of all series',
    responses={200: SeriesSerializer(many=True)},
    auth=[]
)
class SeriesListView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    pagination_class = Pagination


@extend_schema(
    tags=['Series'],
    summary='Details of a series',
    responses={200: SeriesSerializer},
    auth=[]
)
class SeriesDetailView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    lookup_field = 'content__title'
    lookup_url_kwarg = 'title'


class EpisodeDetailView(APIView):
    permission_classes = [AllowAny]
    serializer_class = EpisodeSerializer

    @extend_schema(
        tags=['Series'],
        summary='Details of an episode',
        responses={200: EpisodeSerializer},
        auth=[]
    )
    def get(self, request, episode_number, series):
        try:
            episode = Episode.objects.get(number=episode_number, season__series__content__title=series)

        except Episode.DoesNotExist:
            return Response({'message': 'Episode Not Found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = EpisodeSerializer(instance=episode)
        return Response(serializer.data, status=status.HTTP_200_OK)
