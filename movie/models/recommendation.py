from django.db import models
from account.models import User
from .content import Content


class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recommendations')
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='recommended_to')
    score = models.FloatField(help_text="recommendation score based on algorithm")
    reason = models.CharField(max_length=255, blank=True, null=True)  # reason why a content is recommended
    created_at = models.DateTimeField(auto_now_add=True)
    viewed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'content')
        ordering = ['-score']

    def __str__(self):
        return f"Recommendation of {self.content.title} to {self.user.username}"
