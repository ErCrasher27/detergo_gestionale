# Generated by Django 4.1.5 on 2023-01-08 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detergo_gestionale_app', '0004_category_slug_category_thumbnail_alter_category_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='category',
            name='thumbnail',
        ),
    ]
