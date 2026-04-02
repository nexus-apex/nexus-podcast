from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import PodcastShow, Episode, PodSubscriber
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusPodcast with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexuspodcast.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if PodcastShow.objects.count() == 0:
            for i in range(10):
                PodcastShow.objects.create(
                    title=f"Sample PodcastShow {i+1}",
                    host=f"Sample {i+1}",
                    category=random.choice(["technology", "business", "education", "entertainment", "news", "health"]),
                    episodes=random.randint(1, 100),
                    subscribers=random.randint(1, 100),
                    rating=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["active", "paused", "ended"]),
                    description=f"Sample description for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 PodcastShow records created'))

        if Episode.objects.count() == 0:
            for i in range(10):
                Episode.objects.create(
                    title=f"Sample Episode {i+1}",
                    show_title=f"Sample Episode {i+1}",
                    episode_number=random.randint(1, 100),
                    duration_mins=random.randint(1, 100),
                    published_date=date.today() - timedelta(days=random.randint(0, 90)),
                    downloads=random.randint(1, 100),
                    status=random.choice(["draft", "scheduled", "published", "archived"]),
                    audio_url=f"https://example.com/{i+1}",
                    description=f"Sample description for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 Episode records created'))

        if PodSubscriber.objects.count() == 0:
            for i in range(10):
                PodSubscriber.objects.create(
                    name=f"Sample PodSubscriber {i+1}",
                    email=f"demo{i+1}@example.com",
                    subscribed_shows=f"Sample {i+1}",
                    platform=random.choice(["apple", "spotify", "google", "rss", "website"]),
                    subscribed_date=date.today() - timedelta(days=random.randint(0, 90)),
                    status=random.choice(["active", "unsubscribed"]),
                    listens=random.randint(1, 100),
                )
            self.stdout.write(self.style.SUCCESS('10 PodSubscriber records created'))
