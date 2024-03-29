from django.urls import path
from . import views
urlpatterns = [
        # when you go to home pg got to views, and find index func to server
        path('', views.index, name='index'),
        path('signup', views.signup, name='signup'),
        path('login', views.login, name='login'),
        path('logout', views.login, name='logout'),
        path('settings', views.settings, name='settings'),
        path('upload', views.upload, name='upload'),
        path('list', views.list, name='list'),
        path('feed', views.feed, name='feed'),

        path('popularMovies', views.popularMovies, name='popularMovies')
]