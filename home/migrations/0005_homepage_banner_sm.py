# Generated by Django 4.2.14 on 2024-08-13 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0026_delete_uploadedimage'),
        ('home', '0004_homepage_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_sm',
            field=models.ForeignKey(blank=True, help_text='Banner para mostrar al inicio del blog en tamaño mobile', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Banner Home SM'),
        ),
    ]