from django.test import TestCase
from django.core.urlresolvers import reverse

class TestViews(TestCase):

    def test_home_page(self):
        """
        Tests the home page appears with no errors
        """
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
