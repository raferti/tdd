from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    """Тест нового посетителя"""

    def setUp(self) -> None:
        """Установка"""
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        """Демонтаж"""
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('todo', self.browser.title)
        self.fail('закончить тест')


if __name__ == '__main__':
    unittest.main(warnings='ignore')