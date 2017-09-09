from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django_markdown.models import MarkdownField
from django.utils import timezone


class Issue(models.Model):
    """An issue is a themed collection of blog entries with accompanying text"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    number = models.IntegerField()
    introduction = models.TextField()
    # TODO make this generic?
    well_image = models.CharField(
        max_length=200,
        blank=True,
        help_text="Image to fill this issue's well (higher "+
                  "priority than 'well text').")
    well_text = models.TextField(
        blank=True,
        help_text="Text to fill this issue's well (if blank, 'issue "+
                  "content' will be used).")
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    """A category is another collection of blog entries."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})


class MainCategory(models.Model):
    """A main-category is one which the user can browse in the top menu. If
    there are none specified, then the categories are ordered by number of
    entries.
    """
    category = models.OneToOneField(Category,
        help_text="This category will appear in the header-menu. If there are "
        "no main-categories then the most popular ones will be displayed.")

    def __str__(self):
        return self.category.title


class Entry(models.Model):
    """An single magazine entry."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    content = MarkdownField()
    well_image = models.CharField(
        max_length=200,
        blank=True,
        help_text="Image to fill this entry's well (higher "+
                  "priority than 'well text').")
    well_text = models.TextField(
        blank=True,
        help_text="Text to fill this entry's well (if blank, 'entry "+
                  "content' will be used).")
    issue = models.ForeignKey(Issue, blank=True, null=True)
    categories = models.ManyToManyField(Category)
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def categories_display(self):
        # This is DB heavy
        return ', '.join(map(str, self.categories.all()))
    categories_display.short_description = 'Categories'
