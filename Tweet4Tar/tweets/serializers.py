from rest_framework import serializers
from .models import Tweet
import random




class TweetListSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField('get_likes')
    class Meta:
        model = Tweet
        fields = ['id','content','likes']
    
    def get_likes(self,request):
        return random.randint(0,9999)



    