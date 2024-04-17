from django.forms import model_to_dict
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Post
from ..serializers.post_serializer import PostSerializer


class PostAPIView(APIView):
    def get(self, request):
        queryset = Post.objects.all()
        return Response({'posts': PostSerializer(queryset, many=True).data})

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Post.objects.create(
            title=request.data['title'],
            text=request.data['text'],
            created_date=timezone.now(),
        )
        return Response({'post': PostSerializer(post_new).data})