from django.db import models

from wagtail.core.models import Page, PageManager, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from modelcluster.fields import ParentalKey

from wagtail.core.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

class BlogIndexPage(Page):
    subpage_types = ['blog.BlogPage']

    intro = RichTextField(blank=True, verbose_name='Вступ')

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        
        all_posts = BlogPage.objects.live().public().order_by('-first_published_at')
        context["posts"] = all_posts
        return context

class BlogPage(Page):

    parent_page_types = ['blog.BlogIndexPage']

    date = models.DateField("Post date")
    intro = models.CharField(max_length=250, verbose_name='Про що йде річ')
    # body = RichTextField(blank=True, verbose_name='Основна частина')
    introimage = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, null=True, verbose_name="Прев'ю")

    bodystream = StreamField(
        [
        ('rtfblock',RichTextBlock(template='home/blocks/textblock.html', label='Текст')),
        ('imgblock',ImageChooserBlock(template='home/blocks/imgblock.html', label='Зображення')),
        ('videoblock',EmbedBlock(label='Відео')),
        ],blank=True, verbose_name='Вміст статті')

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
    ]

    content_panels = Page.content_panels + [
        StreamFieldPanel('bodystream'),
        FieldPanel('date'),
        FieldPanel('intro'),
        ImageChooserPanel('introimage'),
        InlinePanel('gallery_images', label="Зображення"),
    ]


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+', verbose_name='Картинка'
    )
    caption = models.CharField(blank=True, max_length=250, verbose_name='Напис')

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
