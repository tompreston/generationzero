from magazine.models import (Issue, Category, Entry)
from django.views.generic import (TemplateView, ListView, DetailView)
from django.shortcuts import get_object_or_404


class SplashPageView(TemplateView):

    template_name = "splash_page.html"

    def get_context_data(self, **kwargs):
        context = super(SplashPageView, self).get_context_data(**kwargs)
        context['issue_list'] = Issue.objects.filter(is_visible=True)
        context['category_list'] = Category.objects.filter(is_visible=True)
        return context


class IssueView(ListView):

    template_name = 'issue.html'
    context_object_name = 'entry_list'

    def get_queryset(self):
        return Entry.objects.filter(issue__slug=self.kwargs['issue_slug'])

    def get_context_data(self, **kwargs):
        context = super(IssueView, self).get_context_data(**kwargs)
        context['issue'] = get_object_or_404(
            Issue,
            slug=self.kwargs['issue_slug'])
        return context


class CategoryView(ListView):

    template_name = 'category.html'
    context_object_name = 'entry_list'

    def get_queryset(self):
        return Entry.objects.filter(
            category__slug=self.kwargs['category_slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['category'] = get_object_or_404(
            Category,
            slug=self.kwargs['category_slug'])
        return context


class EntryDetailView(DetailView):

    template_name = 'entry_detail.html'
    context_object_name = 'entry'

    def get_object(self):
        return get_object_or_404(Entry, slug=self.kwargs['entry_slug'])

    def get_context_data(self, **kwargs):
        context = super(EntryDetailView, self).get_context_data(**kwargs)
        if 'issue_slug' in self.kwargs:
            context['issue'] = get_object_or_404(
                Issue, slug=self.kwargs['issue_slug'])
        elif 'category_slug' in self.kwargs:
            context['category'] = get_object_or_404(
                Category, slug=self.kwargs['category_slug'])
        return context
