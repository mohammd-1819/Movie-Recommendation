from django.urls import path
from .views import content, genre, actor_and_director


app_name = 'movie'

urlpatterns = [
    path('content/all/', content.ContentListView.as_view(), name='content-list'),
    path('content/<str:title>/detail/', content.ContentDetailView.as_view(), name='content-detail'),
    path('content/create/', content.CreatContentView.as_view(), name='content-create'),
    path('content/<str:title>/update/', content.UpdateContentView.as_view(), name='content-update'),
    path('content/<str:title>/remove/', content.RemoveContentView.as_view(), name='content-remove'),
    path('content/movie/all', content.MovieListView.as_view(), name='movie-list'),
    path('content/series/all', content.SeriesListView.as_view(), name='series-list'),


    path('actor-director/all/', actor_and_director.ActorAndDirectorsListView.as_view(), name='actor-director-list'),
    path('actor/all/', actor_and_director.ActorListView.as_view(), name='actor-list'),
    path('director/all/', actor_and_director.DirectorListView.as_view(), name='director-list'),
    path('actor-director/<str:name>/detail/', actor_and_director.ActorOrDirectorDetailView.as_view(),
         name='actor-director-detail'),
    path('actor-director/add/', actor_and_director.AddActorOrDirectorView.as_view(), name='actor-director-add'),
    path('actor-director/<str:name>/update', actor_and_director.UpdateActorOrDirectorView.as_view(),
         name='actor-director-update'),
    path('actor-director/<str:name>/remove', actor_and_director.RemoveActorOrDirectorView.as_view(),
         name='actor-director-remove'),

    path('genre/list/', genre.GenreListView.as_view(), name='genre-list'),
    path('genre/add/', genre.AddGenreView.as_view(), name='genre-add'),
    path('genre/<str:genre>/all/', genre.MovieGenreListView.as_view(), name='genre-movie-list'),
    path('genre/<str:genre>/series/all/', genre.SeriesGenreListView.as_view(), name='genre-series-list'),
]
