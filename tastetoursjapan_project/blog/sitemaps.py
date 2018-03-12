from django.contrib.sitemaps import Sitemap
# from django.contrib.flatpages.models import FlatPage
from .models import Post

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, item):
        return item.publish

# https://matthewdaly.co.uk/blog/2014/08/31/django-blog-tutorial-the-next-generation-part-8/
# class FlatpageSitemap(Sitemap):
#     changefreq = "weekly"
#     priority = 0.9
#     def items(self):
#         return FlatPage.objects.all()
