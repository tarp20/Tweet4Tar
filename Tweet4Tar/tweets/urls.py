from django.urls import path
from .views import tweet_detail_view,home_view,TweetsListApiView

urlpatterns = [
    path('tweet/<int:tweet_id>',tweet_detail_view),
    path('',home_view),
    path('tweets/',TweetsListApiView.as_view())
]
