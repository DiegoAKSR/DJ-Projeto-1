from django.shortcuts import render

from news.models import New
from util.news.factory import make_recipe


def home(request):
    news = New.objects.all().order_by('-id')
    return render(request, 'news/pages/home.html',
                  context={'news': news,

                           })


def category(request, category_id):
    news = New.objects.filter(
        category__id=category_id
    ).order_by('-id')
    return render(request, 'news/pages/home.html',
                  context={'news': news,

                           })


def news(request, id):
    return render(request, 'news/pages/news-view.html',
                  context={'new': make_recipe(),
                           'is_detail_page': True
                           })
