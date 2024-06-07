from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField

# import MultiFieldPanel:
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from post.models import PostPage


class HomePage(Page):

    hero_cta = models.CharField(
        blank=True,
        verbose_name="Hero CTA",
        max_length=255,
        help_text="Texto para mostrar como Call to Action",
    )

    subpage_types = ['post.PostPage']

    # modify your content_panels:
    content_panels = Page.content_panels + [
        FieldPanel("hero_cta"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['posts'] = PostPage.objects.child_of(self).live()
        return context    