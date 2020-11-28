from django.urls import path
from .views import tweet_detail_view,home_view,tweet_list_view

urlpatterns = [
    path('tweet/<int:tweet_id>',tweet_detail_view),
    path('',home_view),
    path('tweets/',tweet_list_view)
]
