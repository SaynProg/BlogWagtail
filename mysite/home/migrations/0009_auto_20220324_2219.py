# Generated by Django 3.2.11 on 2022-03-24 20:19

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_footermodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='footermodel',
            options={'verbose_name': 'Футтер', 'verbose_name_plural': 'Футтери'},
        ),
        migrations.AddField(
            model_name='footermodel',
            name='bodytext',
            field=wagtail.core.fields.RichTextField(default=None, verbose_name='Текст'),
        ),
    ]