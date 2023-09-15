from django.test import TestCase
from django.urls import resolve, reverse

from news import views


class NewViwsTest(TestCase):
    def test_new_home_views_function_is_correct(self):
        view = resolve('/')
        self.assertTrue(view.func.view_class, views.NewsListViewsHome)

    def test_new_search_uses_correct_view_function(self):
        resolved = resolve(reverse('news:search'))
        self.assertIs(resolved.func.view_class, views.NewsListViewsSearch)

    def test_new_search_load_correct_template(self):
        response = self.client.get(reverse('news:search') + '?q=teste')
        self.assertTemplateUsed(response, 'news/pages/search.html')

    def test_news_search_term_is_on_page_title_and_scaped(self):
        url = reverse('news:search') + '?q=<teste>'
        response = self.client.get(url)
        self.assertIn(
            'Search for &quot;&lt;teste&gt;&quot;',
            response.content.decode('utf-8')
        )
