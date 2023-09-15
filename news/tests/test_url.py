from django.test import TestCase
from django.urls import reverse


class NewsURLsTest(TestCase):
    def test_news_home_url_is_correct(self):
        url = reverse('news:home')
        self.assertEqual(url, "/")

    def test_news_category_url_is_correct(self):
        url = reverse('news:category', kwargs={'category_id': 1})
        self.assertEqual(url, "/news/category/1/")

    def test_new_search_url_is_correct(self):
        url = reverse('news:search')
        self.assertEqual(url, "/news/search/")
