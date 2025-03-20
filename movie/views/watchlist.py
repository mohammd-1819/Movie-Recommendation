from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView
from ..models import Watchlist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from ..serializers import WatchlistSerializer
from ..utility.pagination import Pagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


class UserWatchlistView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WatchlistSerializer

    @extend_schema(
        tags=['Watchlist'],
        summary='Retrieve user watchlist',
        responses={200: WatchlistSerializer}
    )
    def get(self, request):
        try:
            user_watchlist = Watchlist.objects.filter(user=request.user)
        except Watchlist.DoesNotExist:
            return Response({'message': 'No Watchlist Found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WatchlistSerializer(user_watchlist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddWatchlistView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WatchlistSerializer

    @extend_schema(
        tags=['Watchlist'],
        summary='Add watchlist',
        responses={201: WatchlistSerializer}
    )
    def post(self, request):
        user = request.user
        content_id = request.data.get('content')

        if Watchlist.objects.filter(user=user, content_id=content_id).exists():
            return Response({'error': 'This content is already in your watchlist.'},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = WatchlistSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'message': 'Watchlist Successfully Added', 'result': serializer.data},
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RemoveWatchlistView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WatchlistSerializer

    @extend_schema(
        tags=['Watchlist'],
        summary='Remove Watchlist',
    )
    def delete(self, request, watchlist_id):
        try:
            user_watchlist = Watchlist.objects.get(id=watchlist_id)
        except Watchlist.DoesNotExist:
            return Response({'message': 'No Watchlist Found'}, status=status.HTTP_404_NOT_FOUND)

        user_watchlist.delete()
        return Response({'message': 'Watchlist Removed'}, status=status.HTTP_200_OK)
