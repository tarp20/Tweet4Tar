from django.shortcuts import render
from .models import Tweet
from django.http import HttpResponse,Http404,JsonResponse
from django.shortcuts import render
from rest_framework import generics
from .serializers import TweetListSerializer


def home_view(request,*args,**kwargs):
    return render(request,'pages/home.html',context={},status=200)


class TweetsListApiView(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetListSerializer




'''
def tweet_list_view(request,*args,**kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{'id': x.id,'content':x.content} for x in qs]
    data = {
        'response':tweets_list
    }
    return JsonResponse(data)
'''


def tweet_detail_view(request,tweet_id,*args,**kwargs):
    data = {
        'id':tweet_id,
   
}
    status = 200
    try:
        obj = Tweet.objects.get(id = tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = 'Not found'
        status = 404
    return JsonResponse(data,status=status)


