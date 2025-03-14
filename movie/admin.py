from django.contrib import admin
from .models import ActorAndDirector, Content, Genre, Rating, Recommendation, Role, Season, Series, Episode, Watchlist


admin.site.register(ActorAndDirector)
admin.site.register(Content)
admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(Role)
admin.site.register(Recommendation)
admin.site.register(Series)
admin.site.register(Season)
admin.site.register(Episode)
admin.site.register(Watchlist)

