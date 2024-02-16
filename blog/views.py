from rest_framework import filters
from rest_framework.generics import ListCreateAPIView

from blog.models import Blog
from blog.paginator import DefaultResultPagination
from blog.serializer import BlogSerializer, CreateBlogSerializer


class ListBlogView(ListCreateAPIView):
    """
       Handle Get and Post request for blogs
       Returns: \n
           A Response object containing list of blog objects.

    """

    queryset = Blog.objects.all()
    pagination_class = DefaultResultPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['category__name', 'tags__name', 'title']

    def get_serializer_class(self):
        if self.request.method == "GET":
            return BlogSerializer
        return CreateBlogSerializer
