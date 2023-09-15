"""
import pytest
from base import NewsBaseTest
from selenium.webdriver.common.by import By


@pytest.mark.functional_test
class NewsHomePageTest(NewsBaseTest):
    def test_news_home_page_not_found_messagens(self):
        browser = self.browser
        browser.get(self.live_server_url)
        body = browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('Não possuimos Posts 😱', body.text)
"""
