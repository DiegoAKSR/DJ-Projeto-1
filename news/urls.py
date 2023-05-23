from django.urls import path

from . import views

app_name = 'news'

urlpatterns = [
    path('', views.home, name="home"),
    path('news/category/<int:category_id>/', views.category, name="category"),
    path('news/<int:id>/', views.news, name="new"),
]
