from django.urls import path

from . import views

app_name = 'authors'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('create/', views.register_create, name='create'),
    path('login/', views.login_view, name='login'),
    path('login/create/', views.login_create, name='login_create'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/new/<int:id>/edit/', views.DashboardNews.as_view(),
         name='dashboard_new_edit'),
    path('dashboard/create/new/', views.DashboardNews.as_view(),
         name='dashboard_create_new'),
    path('dashboard/new/delete/', views.DashboardNewsDelete.as_view(),
         name='dashboard_new_delete'),
]
