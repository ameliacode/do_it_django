from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PostList(ListView): #Class Based View
    model = Post
    ordering = "-pk"

# index.html
# Create your views here. Function Based View
# def index(request):
#     posts = Post.objects.all().order_by("-pk")
#
#     return render(
#         request,
#         "blog/post_list.html",
#         {
#             "posts" : posts,
#         }
#     )
#
# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         "blog/single_post_page.html",
#         {
#             "post" : post,
#         }
#     )
