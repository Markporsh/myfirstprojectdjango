from django.contrib.auth import admin
from django.urls import path, include
from myblog import settings
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('blog.urls')),
]


if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns


handler404 = pageNotFound
