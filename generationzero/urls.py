"""generationzero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import (url, include)
# from django.contrib import admin
from magazine.admin import admin_site
from magazine import urls as magazine_urls


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^admin/', admin_site.urls),
    url(r'', include(magazine_urls)),
    url('^markdown/', include( 'django_markdown.urls')),
]
