from test_plus.test import TestCase
from django.test import RequestFactory



# class SitemapTest(TestCase):
#     def test_sitemap(self):
#         # Create a post
#         post = PostFactory()
#         # Create a flat page
#         page = FlatPageFactory()
#         # Get sitemap
#         response = self.client.get('/sitemap.xml')
#         self.assertEquals(response.status_code, 200)
#         # Check post is present in sitemap
#         self.assertTrue('my-first-post' in response.content)
#         # Check page is present in sitemap
#         self.assertTrue('/about/' in response.content)
