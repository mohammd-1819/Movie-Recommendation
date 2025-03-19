from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView
from ..models import Rating, Content
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from ..serializers import RatingSerializer
from ..utility.pagination import Pagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


class ContentRatingListView(APIView, Pagination):
    permission_classes = [AllowAny]
    serializer_class = RatingSerializer

    @extend_schema(
        tags=['Rating'],
        summary='All ratings of a content',
        responses={200: RatingSerializer(many=True)},
        auth=[]
    )
    def get(self, request, content_title):
        ratings = Rating.objects.filter(content__title=content_title)
        result = self.paginate_queryset(ratings, request)
        serializer = RatingSerializer(result, many=True)
        return self.get_paginated_response(serializer.data)


class AddRatingView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RatingSerializer

    @extend_schema(
        tags=['Rating'],
        summary='Add a Rating',
        responses={201: RatingSerializer}
    )
    def post(self, request, content_title):
        try:
            content = Content.objects.get(title=content_title)
        except Content.DoesNotExist:
            return Response({"error": "Content not found"}, status=status.HTTP_404_NOT_FOUND)

        existing_rating = Rating.objects.filter(user=request.user, content=content).first()
        if existing_rating:
            return Response({"error": "You have already rated this content."},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, content=content)
            return Response({'message': 'Rating Successfully Added', 'result': serializer.data},
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    tags=['Rating'],
    summary='Remove a rating (Admin Only)',
)
class RemoveRatingView(DestroyAPIView):
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    lookup_field = 'id'
