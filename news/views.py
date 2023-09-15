import os
from typing import Any

from django.db import models
from django.db.models import Q
from django.http import Http404
from django.views.generic import DetailView, ListView

from news.models import New
from utils.pagination import make_pagination

PER_PAGE = int(os.environ.get('PER_PAGE', 6))


class NewsListViewsBase(ListView):
    model = New
    paginate_by = None
    context_object_name = 'news'
    ordering = ['-id']
    template_name = 'news/pages/home.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            is_published=True,
        )

        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        page_object, pagination_range = make_pagination(
            self.request,
            ctx.get('news'),
            PER_PAGE)
        ctx.update({
            'news': page_object,
            'pagination_range': pagination_range,
        })

        return ctx


class NewsListViewsHome(NewsListViewsBase):
    template_name = 'news/pages/home.html'


class NewsListViewsCategory(NewsListViewsBase):
    template_name = 'news/pages/category.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            category__id=self.kwargs.get('category_id')
        )

        if not qs:
            raise Http404

        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx.update({
            'title': f'{ctx.get("news")[0].category.name} - Category'

        })

        return ctx


class NewsListViewsSearch(NewsListViewsBase):
    template_name = 'news/pages/search.html'

    def get_queryset(self, *args, **kwargs):
        search_term = self.request.GET.get('q', '')
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            Q(
                Q(title__icontains=search_term) |
                Q(description__icontains=search_term) |
                Q(slug__icontains=search_term) |
                Q(text_post__icontains=search_term),
            )

        )

        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        search_term = self.request.GET.get('q', '')
        ctx.update({
            'page_title': f'Search for "{search_term}"',
            'search_term': search_term,
            'additional_url_query': f'&q={search_term}'
        })

        return ctx


class NewsListViewsGames(NewsListViewsBase):
    template_name = 'news/pages/games.html'


class NewsListViewsStorys(NewsListViewsBase):
    template_name = 'news/pages/story.html'


class NewsDetail(DetailView):
    model = New
    context_object_name = 'new'
    template_name = 'news/pages/news-view.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(is_published=True)
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx.update({
            'is_detail_page': True
        })

        return ctx
