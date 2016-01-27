from django.contrib import admin
from magazine.models import (Issue, Category, Entry)


class MagazineAdminSite(admin.AdminSite):

    site_header = 'Magazine administration'


class IssueAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'is_visible')
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'is_visible')
    prepopulated_fields = {"slug": ("title",)}


class EntryAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'issue', 'category', 'is_visible')
    prepopulated_fields = {"slug": ("title",)}


admin_site = MagazineAdminSite(name='magazine_admin')
admin_site.register(Issue, IssueAdmin)
admin_site.register(Category, CategoryAdmin)
admin_site.register(Entry, EntryAdmin)
