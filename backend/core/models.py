from django.db import models

class PodcastShow(models.Model):
    title = models.CharField(max_length=255)
    host = models.CharField(max_length=255, blank=True, default="")
    category = models.CharField(max_length=50, choices=[("technology", "Technology"), ("business", "Business"), ("education", "Education"), ("entertainment", "Entertainment"), ("news", "News"), ("health", "Health")], default="technology")
    episodes = models.IntegerField(default=0)
    subscribers = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("paused", "Paused"), ("ended", "Ended")], default="active")
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Episode(models.Model):
    title = models.CharField(max_length=255)
    show_title = models.CharField(max_length=255, blank=True, default="")
    episode_number = models.IntegerField(default=0)
    duration_mins = models.IntegerField(default=0)
    published_date = models.DateField(null=True, blank=True)
    downloads = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[("draft", "Draft"), ("scheduled", "Scheduled"), ("published", "Published"), ("archived", "Archived")], default="draft")
    audio_url = models.URLField(blank=True, default="")
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class PodSubscriber(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, default="")
    subscribed_shows = models.CharField(max_length=255, blank=True, default="")
    platform = models.CharField(max_length=50, choices=[("apple", "Apple"), ("spotify", "Spotify"), ("google", "Google"), ("rss", "RSS"), ("website", "Website")], default="apple")
    subscribed_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("unsubscribed", "Unsubscribed")], default="active")
    listens = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
