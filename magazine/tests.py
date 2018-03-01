from django.contrib.auth.models import User
from django.test import TestCase
from django.test import Client

from django.urls import reverse

from .models import Entry


class HomePageTests(TestCase):

    def setUp(self):
        for i in range(50):
            User.objects.create(username=f"fakeface{i}")

    def add_entry(self, title, creator):
        Entry.objects.create(title=title, created_by=creator)

    def test_no_entries(self):
        """Test the page loads with no entries"""
        response = self.client.get(reverse("home_page"))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "grid-item")

    def test_entires(self):
        """Test the page loads with some entries"""
        entries_per_user = 10
        for user in User.objects.all():
            for i in range(entries_per_user):
                self.add_entry(f"An entry number {i} by {user.username}", user)

        response = self.client.get(reverse("home_page"))
        self.assertEqual(response.status_code, 200)
        expected_entries = User.objects.count() * entries_per_user
        self.assertContains(response, "grid-item", count=expected_entries)
