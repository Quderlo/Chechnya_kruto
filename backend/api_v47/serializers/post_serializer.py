from rest_framework import serializers
from api_v47.models.post import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'text', 'author')