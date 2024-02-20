from django.shortcuts import render

from rest_framework import pagination
from rest_framework import viewsets

from .models import Post
from .serializers import PostSerializer


def index(request):
    return render(request, 'posts/index.html')


class PostNumberPagination(pagination.PageNumberPagination):
    page_size = 5


class PostViewSet(viewsets.ModelViewSet):
    pagination_class = PostNumberPagination
    queryset = Post.objects.all()
    serializer_class = PostSerializer