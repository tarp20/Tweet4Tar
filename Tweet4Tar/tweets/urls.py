from django.urls import path
from .views import home_view,TweetsListApiView, tweet_detail_view,tweet_create_view

urlpatterns = [
    path('tweet/<int:tweet_id>',tweet_detail_view),
    path('',home_view,name='home'),
    path('api/tweets/',TweetsListApiView.as_view()),
    path('create-tweet/',tweet_create_view),
]
