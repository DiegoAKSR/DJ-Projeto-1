from django.urls import path

from . import views

app_name = 'news'

urlpatterns = [
    path('', views.NewsListViewsHome.as_view(), name="home"),
    path('news/search/', views.NewsListViewsSearch.as_view(), name="search"),
    path('news/games', views.NewsListViewsGames.as_view(), name="games"),
    path('news/storys', views.NewsListViewsStorys.as_view(), name="storys"),
    path('news/category/<int:category_id>/',
         views.NewsListViewsCategory.as_view(), name="category"),
    path('news/<int:pk>/', views.NewsDetail.as_view(), name="new"),



]
