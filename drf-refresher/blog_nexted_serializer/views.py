from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import BlogSerializer, CommentSerializer
from .models import Blog, Comment
# Create your views here.




#=====Blog Generics ONLY LIST VIEW=====#
class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


#====Blog Generics ONLY DETAIL VIEW=====#
class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
   
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer    
    lookup_field = 'pk'



#=====Comment Generics ONLY LIST VIEW=====#
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


#====Comment Generics ONLY DETAIL VIEW=====#
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk' 
   