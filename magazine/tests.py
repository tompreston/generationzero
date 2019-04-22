from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from .models import Category, Entry

NUM_CATEGORIES = 100

class CategoryTests(object):

    def category_setup(self):
        c = (Category(title=f"fake-category{i}", slug=f"fake-category{i}")
             for i in range(NUM_CATEGORIES))
        Category.objects.bulk_create(c)

    def category_test(self, response):
        with open('/tmp/test.html', 'w') as f:
            f.write(str(response.content))
        # We expect six categories at the top, then each category listed in the
        # drop-down for mobile devices. Each category has a name + link so the
        # total is doubles
        exp_num_categories = (6 + NUM_CATEGORIES) * 2
        self.assertContains(response, "fake-category", count=exp_num_categories)

class HomePageTests(TestCase, CategoryTests):

    def setUp(self):
        for i in range(50):
            User.objects.create(username=f"fakeface{i}")
        self.category_setup()

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

    def test_categories(self):
        response = self.client.get(reverse("home_page"))
        self.assertEqual(response.status_code, 200)
        self.category_test(response)
