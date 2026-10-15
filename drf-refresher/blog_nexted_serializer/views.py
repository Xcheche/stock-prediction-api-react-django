from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import BlogSerializer, CommentSerializer
from .models import Blog, Comment
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.


# =====Blog Generics ONLY LIST VIEW=====#
class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [SearchFilter, OrderingFilter]  # Enable search and ordering filters
    search_fields = ['title', 'content']  # Allow searching by title and content
    # Using wildcard search for more flexible searching, allowing partial matches and case-insensitive searches.
    # search_fields = ['^title']
    ordering_fields = ['id', 'created_at', 'title']  # Allow ordering by Id and created_at different from default ordering by created_at field in the model, remeber this will overide created_at ordering in the model. You can also use ordering = ['-created_at'] to order by created_at field in descending order.


# ====Blog Generics ONLY DETAIL VIEW=====#
class BlogDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "pk"


# =====Comment Generics ONLY LIST VIEW=====#
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# ====Comment Generics ONLY DETAIL VIEW=====#
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "pk"
