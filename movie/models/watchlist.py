from django.db import models
from .content import Content


class Watchlist(models.Model):
    user = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='watchlist')
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='in_watchlists')
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'content')

    def __str__(self):
        return f"{self.content.title} in {self.user.username}'s watchlist"
