import os
import sys
# add current path to sys direction (project root)
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'generationzero.settings'
import django
django.setup()

from django.utils.text import slugify

from magazine.models import Category


CATEGORY_TITLES = ['Art',
                   'Design',
                   'Music',
                   'Writing',
                   'Film',
                   'Digital',
                   'Travel']


if __name__ == '__main__':
    categories = [Category(title=title, slug=slugify(title))
                  for title in CATEGORY_TITLES]
    print("Adding:")
    for category in categories:
        print(category.title)
    Category.objects.bulk_create(categories)
