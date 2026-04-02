from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('podcastshows/', views.podcastshow_list, name='podcastshow_list'),
    path('podcastshows/create/', views.podcastshow_create, name='podcastshow_create'),
    path('podcastshows/<int:pk>/edit/', views.podcastshow_edit, name='podcastshow_edit'),
    path('podcastshows/<int:pk>/delete/', views.podcastshow_delete, name='podcastshow_delete'),
    path('episodes/', views.episode_list, name='episode_list'),
    path('episodes/create/', views.episode_create, name='episode_create'),
    path('episodes/<int:pk>/edit/', views.episode_edit, name='episode_edit'),
    path('episodes/<int:pk>/delete/', views.episode_delete, name='episode_delete'),
    path('podsubscribers/', views.podsubscriber_list, name='podsubscriber_list'),
    path('podsubscribers/create/', views.podsubscriber_create, name='podsubscriber_create'),
    path('podsubscribers/<int:pk>/edit/', views.podsubscriber_edit, name='podsubscriber_edit'),
    path('podsubscribers/<int:pk>/delete/', views.podsubscriber_delete, name='podsubscriber_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
