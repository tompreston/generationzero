from magazine.models import (Issue, MainCategory, Category, Entry)
from django.views.generic import (TemplateView, ListView, DetailView)
from django.views.generic.base import ContextMixin
from django.shortcuts import get_object_or_404
from django.db.models import Count


class CategoriesContextMixin(ContextMixin):

    MAX_NUM_DEFAULT_CATEGORIES = 6

    def get_context_data(self, **kwargs):
        context = super(
            CategoriesContextMixin, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.filter(is_visible=True)
        context['main_category_list'] = self.get_main_category_list()
        return context

    def get_main_category_list(self):
        """Returns a list of main categories ordered alphabetically by title.
        This list is either specified in admin or the categories with the most
        entries.
        """
        # TODO maybe make this some kind of try/except
        # give me all the categories in the main category list
        main_category_list = Category.objects.filter(
                maincategory__pk__gt = 0).order_by('title')
        if len(main_category_list) == 0:
            main_category_list = self.get_popular_categories()
        return main_category_list

    def get_popular_categories(self):
        """Return a list of the most popular categories."""
        return Category.objects.annotate(
                num_entries=Count('entry')
            ).order_by(
                '-num_entries'
            )[:self.MAX_NUM_DEFAULT_CATEGORIES]


class HomePageView(CategoriesContextMixin, TemplateView):

    template_name = "magazine/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['category'] = self.get_category()
        context['entry_list'] = self.get_entry_list()
        context['issue_list'] = Issue.objects.filter(is_visible=True)
        return context

    def get_category(self):
        return self.kwargs.get('category_slug')

    def get_entry_list(self):
        entries = Entry.objects.filter(is_visible=True)\
                               .order_by('-created_at')
        category = self.get_category()
        if category:
            entries = entries.filter(categories__slug=category)
        return entries


class IssueView(CategoriesContextMixin, ListView):

    template_name = 'magazine/issue_detail.html'
    context_object_name = 'entry_list'

    def get_queryset(self):
        return Entry.objects.filter(issue__slug=self.kwargs['issue_slug'])

    def get_context_data(self, **kwargs):
        context = super(IssueView, self).get_context_data(**kwargs)
        context['issue'] = get_object_or_404(
            Issue,
            slug=self.kwargs['issue_slug'])
        return context


class IssueListView(CategoriesContextMixin, ListView):

    template_name = 'magazine/issue_list.html'
    context_object_name = 'issue_list'

    def get_queryset(self):
        return Issue.objects.filter(is_visible=True)


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
