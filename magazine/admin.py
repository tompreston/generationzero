from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from magazine.models import (Issue, Category, Entry)


class MagazineAdminSite(admin.AdminSite):

    site_header = 'Magazine administration'


class UserAdmin(admin.ModelAdmin):

    list_display = ('username',
                    'first_name',
                    'last_name',
                    'email',
                    'date_joined',
                    'last_login',
                    'is_superuser')


class IssueAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'is_visible')
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'is_visible')
    prepopulated_fields = {"slug": ("title",)}


class EntryAdmin(admin.ModelAdmin):

    list_display = ('title',
                    'slug',
                    'issue',
                    'categories_display',
                    'is_visible')
    prepopulated_fields = {"slug": ("title",)}


admin_site = MagazineAdminSite(name='magazine_admin')
admin_site.register(User, UserAdmin)
# admin_site.register(Group)
admin_site.register(Issue, IssueAdmin)
admin_site.register(Category, CategoryAdmin)
admin_site.register(Entry, EntryAdmin)
