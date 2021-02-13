from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.PostDetail.as_view()),
    path("",views.PostList.as_view()),

    #Function Based View using post_detail.html
    #path("<int:pk>/", views.single_post_page),
    #path("",views.index),
    #path("",views.PostList.as_view()),
]