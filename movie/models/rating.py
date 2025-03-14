from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from account.models import User
from .content import Content


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'content')

    def __str__(self):
        return f"{self.user.username}: {self.rating}/10 for {self.content.title}"
