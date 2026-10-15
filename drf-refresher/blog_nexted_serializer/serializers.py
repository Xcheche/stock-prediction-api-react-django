from rest_framework.serializers import ModelSerializer
from .models import Blog, Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "content", "created_at", "blog"]


class BlogSerializer(ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ["id", "title", "content", "created_at", "comments"]
