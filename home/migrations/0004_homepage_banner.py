# Generated by Django 4.2.14 on 2024-08-13 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0026_delete_uploadedimage'),
        ('home', '0003_homepage_hero_cta'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner',
            field=models.ForeignKey(blank=True, help_text='Banner para mostrar al inicio del blog', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Banner Home'),
        ),
    ]
