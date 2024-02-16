from django.db import models
from django.utils.translation import gettext_lazy as _


class CreatedUpdatedSoftDeleteMixin(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        auto_now_add=True, help_text=_("The creation time")
    )

    updated_at = models.DateTimeField(
        auto_now=True, help_text=_("The last update time")
    )
    is_updated = models.BooleanField(default=False)


class Category(CreatedUpdatedSoftDeleteMixin):
    """
    Model: Category model Stores different categories of blogs
    """

    name = models.CharField(max_length=70)

    def __str__(self) -> str:
        return self.name


class Tag(CreatedUpdatedSoftDeleteMixin):
    """
    Model: Tag model Stores different tags of blogs
    """

    name = models.CharField(max_length=70)

    def __str__(self) -> str:
        return self.name


class Blog(CreatedUpdatedSoftDeleteMixin):
    title = models.CharField(max_length=70)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    tags = models.ManyToManyField(Tag, blank=True, related_name="tags")
    is_draft = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
