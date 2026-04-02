from django.contrib import admin
from .models import PodcastShow, Episode, PodSubscriber

@admin.register(PodcastShow)
class PodcastShowAdmin(admin.ModelAdmin):
    list_display = ["title", "host", "category", "episodes", "subscribers", "created_at"]
    list_filter = ["category", "status"]
    search_fields = ["title", "host"]

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ["title", "show_title", "episode_number", "duration_mins", "published_date", "created_at"]
    list_filter = ["status"]
    search_fields = ["title", "show_title"]

@admin.register(PodSubscriber)
class PodSubscriberAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subscribed_shows", "platform", "subscribed_date", "created_at"]
    list_filter = ["platform", "status"]
    search_fields = ["name", "email", "subscribed_shows"]
