from rest_framework import serializers

from blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    tag_names = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['title', 'category_name', 'tag_names', 'is_draft']

    def get_category_name(self, obj):
        return obj.category.name

    def get_tag_names(self, obj):
        return list(obj.tags.values_list('name', flat=True))


class CreateBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'category', 'tags', 'is_draft']
