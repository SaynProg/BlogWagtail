# Generated by Django 3.2.11 on 2022-03-24 20:09

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_blogpage_introimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogindexpage',
            name='intro',
            field=wagtail.core.fields.RichTextField(blank=True, verbose_name='Вступ'),
        ),
    ]