from django.db.models import Avg
from ..models import Rating, Content, Recommendation, Genre
from datetime import timedelta, date


def generate_recommendations(user):
    watched_content = Rating.objects.filter(user=user).values_list('content_id', flat=True)
    unwatched_content = Content.objects.exclude(id__in=watched_content)

    recommended_content = (
        unwatched_content.annotate(avg_rating=Avg('ratings__rating'))
        .filter(avg_rating__gte=7)
        .order_by('-avg_rating')[:10]
    )

    Recommendation.objects.filter(user=user).delete()
    for content in recommended_content:
        Recommendation.objects.create(user=user, content=content)

    return recommended_content


def recommend_by_genre(user):
    favorite_genres = (
        Genre.objects.filter(contents__ratings__user=user)
        .annotate(avg_rating=Avg('contents__ratings__rating'))
        .order_by('-avg_rating')[:3]
    )

    watched_content = Rating.objects.filter(user=user).values_list('content_id', flat=True)
    recommended_content = (
        Content.objects.filter(genres__in=favorite_genres)
        .exclude(id__in=watched_content)
        .distinct()
        .order_by('-release_date')[:10]
    )

    return recommended_content


def hybrid_recommendations(user):
    Recommendation.objects.filter(user=user).delete()

    cf_recommendations = list(generate_recommendations(user))
    genre_recommendations = list(recommend_by_genre(user))

    combined_recommendations = cf_recommendations.copy()

    for content in genre_recommendations:
        if content not in combined_recommendations:
            combined_recommendations.append(content)

    for content in combined_recommendations:

        if content.release_date >= date.today() - timedelta(days=30):
            reason = "New release"
        elif content in genre_recommendations:
            reason = 'Based on Favorite Genres'
        elif content.average_rating() >= 4.5:
            reason = "Highly rated by users"
        else:
            reason = "Recommended based on your watch history"

        # ایجاد توصیه در دیتابیس
        Recommendation.objects.create(user=user, content=content, reason=reason)

    return combined_recommendations
