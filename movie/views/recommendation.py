from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView
from ..models import Recommendation
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from ..serializers import RecommendationSerializer
from ..utility.pagination import Pagination
from ..utility.recommendation import hybrid_recommendations
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


class HybridRecommendationView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RecommendationSerializer

    @extend_schema(
        tags=['Recommendation'],
        summary='Recommend content to user',
        responses={200: RecommendationSerializer}
    )
    def get(self, request):
        user = request.user

        hybrid_recommendations(user)

        recommendations = Recommendation.objects.filter(user=user)
        serializer = RecommendationSerializer(recommendations, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
