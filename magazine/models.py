from django.db import models
from django.contrib.auth.models import User
from django_markdown.models import MarkdownField
from django.utils import timezone


class Issue(models.Model):
    """An issue is a collection of blog entries."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
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


class Entry(models.Model):
    """An single magazine entry."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    content = MarkdownField()
    issue = models.ForeignKey(Issue, blank=True, null=True)
    category = models.ForeignKey(Category)
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title
