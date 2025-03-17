from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView
from ..models import Content
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from ..serializers import ContentSerializer, CreateContentSerializer
from ..utility.pagination import Pagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser


@extend_schema(
    tags=['Content'],
    summary="List of all contents (Movies and Series)",
    responses={200: ContentSerializer(many=True)},
    auth=[]
)
class ContentListView(ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    pagination_class = Pagination


@extend_schema(
    tags=['Content'],
    summary='detail of a content',
    responses={200: ContentSerializer},
    auth=[]
)
class ContentDetailView(RetrieveAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_field = 'title'


class CreatContentView(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated]
    serializer_class = CreateContentSerializer

    @extend_schema(
        tags=['Content'],
        summary='Create a new content (Admin Only)',
        responses={201: CreateContentSerializer}

    )
    def post(self, request):
        serializer = CreateContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Content Successfully Added', 'result': serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateContentView(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated]
    serializer_class = CreateContentSerializer

    @extend_schema(
        tags=['Content'],
        summary='Update a Content',
        responses={200: CreateContentSerializer}
    )
    def put(self, request, title):
        try:
            content = Content.objects.get(title=title)
        except Content.DoesNotExist:
            return Response({'error': 'Content Not Found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CreateContentSerializer(instance=content, data=request.data, partial=True)
        if serializer.is_valid():
            return Response({'message': 'Content Successfully Updated', 'result': serializer.data},
                            status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    tags=['Content'],
    summary='Remove a content'
)
class RemoveContentView(DestroyAPIView):
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_field = 'title'


@extend_schema(
    tags=['Content'],
    summary="List of all movies",
    responses={200: ContentSerializer(many=True)},
    auth=[]
)
class MovieListView(ListAPIView):
    queryset = Content.objects.filter(content_type='movie')
    serializer_class = ContentSerializer
    pagination_class = Pagination


@extend_schema(
    tags=['Content'],
    summary="List of all series",
    responses={200: ContentSerializer(many=True)},
    auth=[]
)
class SeriesListView(ListAPIView):
    queryset = Content.objects.filter(content_type='series')
    serializer_class = ContentSerializer
    pagination_class = Pagination
