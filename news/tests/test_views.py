from django.test import TestCase
from django.urls import resolve, reverse

from news import views


class NewViwsTest(TestCase):
    def test_new_home_views_function_is_correct(self):
        view = resolve('/')
        self.assertTrue(view.func, views.home)

    def test_new_search_uses_correct_view_function(self):
        resolved = resolve(reverse('news:search'))
        self.assertIs(resolved.func, views.search)

    def test_new_search_load_correct_template(self):
        response = self.client.get(reverse('news:search') + '?q=teste')
        self.assertTemplateUsed(response, 'news/pages/search.html')

    def test_news_search_raises_404_if_no_search_term(self):
        response = self.client.get(reverse('news:search'))
        self.assertEqual(response.status_code, 404)

    def test_news_search_term_is_on_page_title_and_scaped(self):
        url = reverse('news:search') + '?q=<teste>'
        response = self.client.get(url)
        self.assertIn(
            'Search for &quot;&lt;teste&gt;&quot;',
            response.content.decode('utf-8')
        )
