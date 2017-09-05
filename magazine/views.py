from magazine.models import (Issue, MainCategory, Category, Entry)
from django.views.generic import (TemplateView, ListView, DetailView)
from django.views.generic.base import ContextMixin
from django.shortcuts import get_object_or_404


class CategoriesContextMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super(
            CategoriesContextMixin, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.filter(is_visible=True)
        context['main_category_list'] = MainCategory.objects.order_by(
                'category__title')
        return context


class HomePageView(CategoriesContextMixin, TemplateView):

    template_name = "magazine/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['entry_list'] = self.get_entry_list()
        context['issue_list'] = Issue.objects.filter(is_visible=True)
        return context

    def get_entry_list(self):
        entries = Entry.objects.filter(is_visible=True)\
                               .order_by('-created_at')
        category = self.kwargs.get('category_slug')
        if category:
            entries = entries.filter(categories__slug=category)
        return entries



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


# class CategoryView(ListView):

#     template_name = 'category.html'
#     context_object_name = 'entry_list'

#     def get_queryset(self):
#         return Entry.objects.filter(
#             categories__slug=self.kwargs['category_slug'])

#     def get_context_data(self, **kwargs):
#         context = super(CategoryView, self).get_context_data(**kwargs)
#         context['category'] = get_object_or_404(
#             Category,
#             slug=self.kwargs['category_slug'])
#         return context


class EntryDetailView(CategoriesContextMixin, DetailView):

    template_name = 'magazine/entry_detail.html'
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
