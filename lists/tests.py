from django.test import TestCase
from django.urls import resolve
from lists.views import home_page


class SmokeTest(TestCase):
    """Тест домашней страницы"""

    def test_root_url_resolves_to_home_page(self):
        """Тест корневой url преобразуется в представления"""
        found = resolve('/')
        self.assertEqual(found.func, home_page)



