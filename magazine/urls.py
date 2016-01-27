from django.conf.urls import url
from django.views.generic.dates import ArchiveIndexView

from magazine.models import Entry
from magazine.views import (SplashPageView, IssueView, CategoryView,
                            EntryDetailView)


urlpatterns = [
    url(r'^$',
        SplashPageView.as_view(),
        name="splash_page"),

    url(r'^issue/(?P<issue_slug>[\w-]+)/$',
        IssueView.as_view(),
        name="issue"),

    # entry in issue
    url(r'^issue/(?P<issue_slug>[\w-]+)/(?P<entry_slug>[\w-]+)/$',
        EntryDetailView.as_view(),
        name="entry_in_issue"),

    url(r'^category/(?P<category_slug>[\w-]+)/$',
        CategoryView.as_view(),
        name="category"),

    # entry in category
    url(r'^category/(?P<category_slug>[\w-]+)/(?P<entry_slug>[\w-]+)/$',
        EntryDetailView.as_view(),
        name="entry_in_category"),

    # just a single entry
    url(r'^entry/(?P<entry_slug>[\w-]+)/$',
        EntryDetailView.as_view(),
        name="entry"),

    # TODO
    # url(r'^archive/$',
    #     ArchiveIndexView.as_view(model=Entry, date_field="created_at"),
    #     name="entry_archive"),
]
