from rest_framework import generics

from ..models import Post
from ..serializers.post_serializer import PostSerializer


class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer