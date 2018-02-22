from django.test import TestCase
from django.test import Client

from django.urls import reverse


class HomePageTests(TestCase):

    def test_no_entries(self):
        """
        Test the page loads with no entries
        """
        response = self.client.get(reverse("home_page"))
        self.assertEqual(response.status_code, 200)
        """
        print(response.content)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
        """
