from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField

# import MultiFieldPanel:
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from post.models import PostPage


class HomePage(Page):

    banner = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Banner Home",
        help_text="Banner para mostrar al inicio del blog",
    )
    banner_sm = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Banner Home SM",
        help_text="Banner para mostrar al inicio del blog en tamaño mobile",
    )    

    hero_cta = models.CharField(
        blank=True,
        verbose_name="Hero CTA",
        max_length=255,
        help_text="Texto para mostrar como Call to Action",
    )

    subpage_types = ['post.PostPage']

    # modify your content_panels:
    content_panels = Page.content_panels + [
        FieldPanel('banner'),  
        FieldPanel('banner_sm'),        
        FieldPanel("hero_cta"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['posts'] = PostPage.objects.child_of(self).live()
        return context    