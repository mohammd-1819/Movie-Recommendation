from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView
from ..models import Genre, Content
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from ..serializers import GenreSerializer, ContentSerializer
from ..utility.pagination import Pagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


@extend_schema(
    tags=['Genre'],
    summary='List of all genres',
    responses={200: GenreSerializer(many=True)},
    auth=[]
)
class GenreListView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = Pagination


class AddGenreView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = GenreSerializer

    @extend_schema(
        tags=['Genre'],
        summary='Add a new genre (Admin Only)',
        responses={201: GenreSerializer}
    )
    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'New Genre Added Successfully', 'result': serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieGenreListView(APIView, Pagination):
    permission_classes = [AllowAny]
    serializer_class = ContentSerializer

    @extend_schema(
        tags=['Genre'],
        summary='List of all movies in a specific genre',
        responses={200: ContentSerializer(many=True)},
        auth=[]
    )
    def get(self, request, genre):
        movies = Content.objects.filter(content_type='movie', genres__name=genre)
        result = self.paginate_queryset(movies, request)
        serializer = ContentSerializer(result, many=True)
        return self.get_paginated_response(serializer.data)


class SeriesGenreListView(APIView, Pagination):
    permission_classes = [AllowAny]
    serializer_class = ContentSerializer

    @extend_schema(
        tags=['Genre'],
        summary='List of all series in a specific genre',
        responses={200: ContentSerializer(many=True)},
        auth=[]
    )
    def get(self, request, genre):
        series = Content.objects.filter(content_type='series', genres__name=genre)
        result = self.paginate_queryset(series, request)
        serializer = ContentSerializer(result, many=True)
        return self.get_paginated_response(serializer.data)
