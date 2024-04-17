from rest_framework import serializers
from api_v47.models.post import Post


class PostSerializer(serializers.Serializer):
    title = serializers.CharField()
    text = serializers.CharField()
    created_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Post
        fields = (
            'title',
            'text',
            'create_date',
        )

    def create(self, validated_data):
        return Post.objects.create(**validated_data)