from django.db.models import Count
from .models import *


menu = [{'title': 'Homepage', 'url_name': 'home'},
        {'title': 'Blog', 'url_name': 'blog'},
        {'title': 'Add post', 'url_name': 'create'},
        {'title': 'My resume', 'url_name': 'about'},
        ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('blog'))
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)

        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
