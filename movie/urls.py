from django.urls import path
from .views import content, genre, actor_and_director, rating, series

app_name = 'movie'

urlpatterns = [
    path('all/', content.ContentListView.as_view(), name='content-list'),
    path('<str:title>/detail/', content.ContentDetailView.as_view(), name='content-detail'),
    path('create/', content.CreatContentView.as_view(), name='content-create'),
    path('<str:title>/update/', content.UpdateContentView.as_view(), name='content-update'),
    path('<str:title>/remove/', content.RemoveContentView.as_view(), name='content-remove'),
    path('movie/all', content.MovieListView.as_view(), name='movie-list'),
    path('series/all', content.SeriesListView.as_view(), name='series-list'),

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

    path('rating/<str:content_title>/all', rating.ContentRatingListView.as_view(), name='rating-content-list'),
    path('rating/<str:content_title>/add/', rating.AddRatingView.as_view(), name='rating-add'),
    path('rating/<int:id>/remove/', rating.RemoveRatingView.as_view(), name='rating-remove'),

    path('series/list/', series.SeriesListView.as_view(), name='series-list'),
    path('series/<str:title>/detail/', series.SeriesDetailView.as_view(), name='series-detail'),
    path('series/<str:series>/<int:episode_number>/detail/', series.EpisodeDetailView.as_view(), name='series-episode-detail')
]
