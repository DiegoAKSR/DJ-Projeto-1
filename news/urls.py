from django.urls import path

from . import views

app_name = 'news'

urlpatterns = [
    path('', views.home, name="home"),
    path('news/search/', views.search, name="search"),
    path('news/games', views.games, name="games"),
    path('news/storys', views.storys, name="storys"),
    path('news/category/<int:category_id>/', views.category, name="category"),
    path('news/<int:id>/', views.news, name="new"),



]
