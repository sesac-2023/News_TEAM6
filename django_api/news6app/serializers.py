from rest_framework import serializers
from news6app.models import *
import numpy as np

# Create your serializers here.
class NewsSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = News
        fields = ['id', 'cat2', 'title', 'press', 'writer', 'date_upload', 'content', 'url']
        # fields = "__all__"

class LatestNewsSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = News
        # fields = ['cat2', 'title', 'press', 'writer', 'date_upload', 'content', 'url']
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = User
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Comment
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Category
        fields = "__all__"