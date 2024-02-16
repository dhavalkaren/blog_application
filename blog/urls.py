from django.urls import path

from blog.views import ListBlogView

urlpatterns = [
    path("", ListBlogView.as_view())
]
