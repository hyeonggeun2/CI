from django.test import TestCase


class MainItemTest(TestCase):
    def test_get_items(self):
        response = self.client.get('/main/items/')
