from django.http import Http404
from django.shortcuts import get_object_or_404, render

from news.models import New
from util.news.factory import make_recipe


def home(request):
    news = New.objects.filter(is_published=True).order_by('-id')
    return render(request, 'news/pages/home.html',
                  context={'news': news,
                           })


def category(request, category_id):
    news = New.objects.filter(
        category__id=category_id, is_published=True
    ).order_by('-id')

    if not news:
        raise Http404("Not Found 😱")

    return render(request, 'news/pages/category.html',
                  context={'news': news,
                           'title': f'{news.first().category.name} - Category'

                           })


def news(request, id):
    new = get_object_or_404(New, pk=id, is_published=True)

    return render(request, 'news/pages/news-view.html',
                  context={'new': new,
                           'is_detail_page': True
                           })
