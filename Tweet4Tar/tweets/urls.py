from django.urls import path
from .views import home_view,tweet_list_view, tweet_detail_view,tweet_create_view

urlpatterns = [
    path('tweet/<int:tweet_id>',tweet_detail_view),
    path('',home_view,name='home'),
    path('tweets/',tweet_list_view),
    path('create-tweet/',tweet_create_view),
]
