from . import views
from django.urls import path

app_name = "snowball_blog"

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
]
