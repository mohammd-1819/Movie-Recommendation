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


@extend_schema(
    tags=['Actor And Directors'],
    summary='List of all actors',
    responses={200: ActorAndDirectorSerializer(many=True)},
    auth=[]

)
class ActorListView(ListAPIView):
    queryset = ActorAndDirector.objects.filter(role='actor')
    serializer_class = ActorAndDirectorSerializer
    pagination_class = Pagination


@extend_schema(
    tags=['Actor And Directors'],
    summary='List of all directors',
    responses={200: ActorAndDirectorSerializer(many=True)},
    auth=[]

)
class DirectorListView(ListAPIView):
    queryset = ActorAndDirector.objects.filter(role='director')
    serializer_class = ActorAndDirectorSerializer
    pagination_class = Pagination


@extend_schema(
    tags=['Actor And Directors'],
    summary='Details of an actor or director',
    responses={200: ActorAndDirectorSerializer},
    auth=[]
)
class ActorOrDirectorDetailView(RetrieveAPIView):
    queryset = ActorAndDirector.objects.all()
    serializer_class = ActorAndDirectorSerializer
    lookup_field = 'name'


class AddActorOrDirectorView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ActorAndDirectorSerializer

    @extend_schema(
        tags=['Actor And Directors'],
        summary='Add actor or director (Admin Only)',
        responses={201: ActorAndDirectorSerializer}
    )
    def post(self, request):
        serializer = ActorAndDirectorSerializer(data=request)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Actor or Director Successfully Added', 'result': serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateActorOrDirectorView(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated]
    serializer_class = ActorAndDirectorSerializer

    @extend_schema(
        tags=['Actor And Directors'],
        summary='Update details of an actor or director (Admin Only)',
        responses={200: ActorAndDirectorSerializer}
    )
    def put(self, request, title):
        try:
            actor_or_director = ActorAndDirector.objects.get(title=title)
        except ActorAndDirector.DoesNotExist:
            return Response({'error': 'Actor or Director Not Found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ActorAndDirectorSerializer(instance=actor_or_director, data=request.data, partial=True)
        if serializer.is_valid():
            return Response({'message': 'Actor or Director Successfully Updated', 'result': serializer.data},
                            status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    tags=['Actor And Directors'],
    summary='Remove an actor or director (Admin Only)'
)
class RemoveActorOrDirectorView(DestroyAPIView):
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = ActorAndDirector.objects.all()
    serializer_class = ActorAndDirectorSerializer
    lookup_field = 'name'
