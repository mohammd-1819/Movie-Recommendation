from django.db import models
from .content import Content


class Series(models.Model):
    content = models.OneToOneField(Content, on_delete=models.CASCADE, related_name='series_info')
    seasons_count = models.PositiveIntegerField(default=1)
    episodes_count = models.PositiveIntegerField(default=1)
    ended = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.content.title} - {self.seasons_count} seasons"


class Season(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE, related_name='seasons')
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=200, blank=True, null=True)
    release_date = models.DateField()
    episodes_count = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.series.content.title} - season {self.number}"

    class Meta:
        unique_together = ('series', 'number')
        ordering = ['number']


class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='episodes')
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    duration = models.PositiveIntegerField(help_text="duration of the episode")

    def __str__(self):
        return f"{self.season.series.content.title} - S{self.season.number:02d}E{self.number:02d} - {self.title}"

    class Meta:
        unique_together = ('season', 'number')
        ordering = ['number']
