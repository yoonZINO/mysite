from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ["django_app:index", "django_app:about", "django_app:contact"]

    def location(self, item):
        return reverse(item)