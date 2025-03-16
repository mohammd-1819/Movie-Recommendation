from django.urls import path
from .views import content
from .views import actor_and_director

app_name = 'movie'

urlpatterns = [
    path('content/all/', content.ContentListView.as_view(), name='content-list'),
    path('content/<str:title>/detail/', content.ContentDetailView.as_view(), name='content-detail'),
    path('content/create/', content.CreatContentView.as_view(), name='content-create'),
    path('content/<str:title>/update/', content.UpdateContentView.as_view(), name='content-update'),
    path('content/<str:title>/remove/', content.RemoveContentView.as_view(), name='content-remove'),
    path('content/movie/all', content.MovieListView.as_view(), name='movie-list'),
    path('content/series/all', content.SeriesListView.as_view(), name='series-list'),

    path('actor-director/all/', actor_and_director.ActorAndDirectorsListView.as_view(), name='actor-director-list')
]
