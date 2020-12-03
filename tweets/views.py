from django.shortcuts import render
from django.http import HttpResponse,Http404,JsonResponse,HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render,redirect

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from django.utils.http import is_safe_url
from .forms import TweetForm

from .models import Tweet
from .serializers import TweetSerializer
import random


ALLOWED_HOSTS = settings.ALLOWED_HOSTS

def home_view(request,*args,**kwargs):
    return render(request,'pages/home.html',context={},status=200)


@api_view(['POST'])
#@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def tweet_create_view(request,*args,**kwargs):
    serializer = TweetSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response({},status = 400)

@api_view(['GET'])
def tweet_list_view(request,*args,**kwargs):
    qs = Tweet.objects.all()
    serializer = TweetSerializer(qs,many = True)
    return Response(serializer.data,status= 200)

@api_view(['GET'])
def tweet_detail_view(request,tweet_id,*args,**kwargs):
    qs = Tweet.objects.filter(id = tweet_id)
    if not qs.exists():
        return Response({},status = 404)
    obj = qs.first()
    serializer = TweetSerializer(obj)
    return Response(serializer.data)

@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def tweet_delete_view(request,tweet_id,*args,**kwargs):
    qs = Tweet.objects.filter(id = tweet_id)
    if not qs.exists():
        return Response({},status = 404)
    qs = qs.filter(user=request.user)
    if not qs.exists():
        return Response({'message':'You cannot delete this post'},status = 401)
    obj = qs.first()
    obj.delete()
    return Response({'message':'Tweet has been deleted'},status=200)





# def tweet_create_view_django(request,*args,**kwargs):
#     user = request.user
#     if not request.user.is_authenticated:
#         user = None
#         if request.is_ajax():
#             return JsonResponse({},status=401)
#         return redirect(settings.LOGIN_URL)
#     form  = TweetForm(request.POST or None)
#     next_url = request.POST.get('next') or None
#     if form.is_valid():
#         obj = form.save(commit=False)
#         obj.user = user 
#         obj.save()
#         if request.is_ajax():
#             return JsonResponse(obj.serialize(),status=201)
#         if next_url != None and is_safe_url(next_url,ALLOWED_HOSTS):
#             return redirect(next_url)
#         form  = TweetForm()
#     if form.errors:
#         if request.is_ajax():
#             return JsonResponse(form.errors,status = 400)
#     return render(request,'components/form.html',context={"form":form})


    







'''
def tweet_list_view(request,*args,**kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{'id': x.id,'content':x.content} for x in qs]
    data = {
        'response':tweets_list
    }
    return JsonResponse(data)
'''


# def tweet_detail_view(request,tweet_id,*args,**kwargs):
#     data = {
#         'id':tweet_id,
   
# }
#     status = 200
#     try:
#         obj = Tweet.objects.get(id = tweet_id)
#         data['content'] = obj.content
#     except:
#         data['message'] = 'Not found'
#         status = 404
#     return JsonResponse(data,status=status)


# def tweet_list_view(request,*args,**kwargs):
#     qs = Tweet.objects.all()
#     tweets_list = [ x.serialize() for x in qs]
#     data = {
#         'response':tweets_list
#     }
#     return JsonResponse(data)