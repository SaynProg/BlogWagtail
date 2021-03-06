# Generated by Django 3.2.11 on 2022-03-18 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('blog', '0008_remove_blogpage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='introimage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.image'),
        ),
        migrations.AlterField(
            model_name='blogpagegalleryimage',
            name='caption',
            field=models.CharField(blank=True, max_length=250, verbose_name='Напис'),
        ),
        migrations.AlterField(
            model_name='blogpagegalleryimage',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image', verbose_name='Картинка'),
        ),
    ]
