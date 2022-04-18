from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField, RichTextField

from wagtail.core.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

from wagtail.snippets.models import register_snippet

@register_snippet
class FooterModel(models.Model):

    bodytext = RichTextField(verbose_name='Текст')

    panels = [
        FieldPanel('bodytext'),
    ]

    class Meta:
        verbose_name = 'Футтер'
        verbose_name_plural = 'Футтери'

    def __str__(self):
        return 'Футтер'

class HomePage(Page):

    # template = 'home/home_page.html'
    # body = RichTextField(blank=True)
    
    parent_page_types = []
    # max_count = 1

    bodystream = StreamField(
        [
        ('rtfblock',RichTextBlock(template='home/blocks/textblock.html', label='Текст')),
        ('imgblock',ImageChooserBlock(template='home/blocks/imgblock.html', label='Зображення')),
        ('videoblock',EmbedBlock(label='Відео')),
        ],blank=True, verbose_name='Вміст статті')
    
    # home_image = models.ForeignKey(
    #     'wagtailimages.Image', 
    #     blank=True, null=True, 
    #     on_delete=models.SET_NULL, 
    #     related_name='+',
    #     verbose_name='Зображення сторінки'
    # )

    content_panels = Page.content_panels + [
        StreamFieldPanel('bodystream'),
        # ImageChooserPanel('home_image'),
    ]