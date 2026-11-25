from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils import timezone

from blog.models import Post


class Command(BaseCommand):
    help = "Add two sample posts to the blog."

    def handle(self, *args, **options):
        author, _ = get_user_model().objects.get_or_create(username="sample-author")
        examples = [
            ("My first Django post", "I set up a URL, a view, and an HTML template for this blog."),
            ("Getting posts from SQLite", "The Django ORM loads published posts and sorts them by date."),
        ]

        for title, text in examples:
            Post.objects.get_or_create(
                author=author,
                title=title,
                defaults={"text": text, "published_date": timezone.now()},
            )

        self.stdout.write(self.style.SUCCESS("Sample posts are ready."))
