from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager

from taggit.models import TaggedItemBase

class PostPageTag(TaggedItemBase):
    content_object = ParentalKey('post.PostPage', on_delete=models.CASCADE, related_name='tagged_items')

class PostPage(Page):
    banner = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Banner post",
        help_text="Banner para mostrar al inicio del post",
    )    
    author = models.CharField(
        blank=True,
        verbose_name="Autor/a",
        max_length=70,
        help_text="Agrega un autor/a",
    )    
    date = models.DateField("Fecha")
    tags = ClusterTaggableManager(through=PostPageTag, blank=True)
    abstract = models.CharField(
        blank=True,
        verbose_name="Resumen",
        max_length=255,
        help_text="Agrega un resumen",
    )
    body = RichTextField()
    content_panels = Page.content_panels + [
        FieldPanel('banner'),
        FieldPanel('author'),
        FieldPanel('date'),
        FieldPanel('tags'),
        FieldPanel('abstract'),
        FieldPanel('body'),
    ]

    parent_page_types = ['home.HomePage']

