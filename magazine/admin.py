from django.contrib import admin
from magazine.models import (Issue, Category, Entry)


class IssueAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class EntryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Issue, IssueAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)
