# Generated by Django 4.1.5 on 2023-01-08 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detergo_gestionale_app', '0007_category_maxi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='maxi',
            field=models.CharField(choices=[('LE', 'left'), ('RI', 'right')], max_length=2),
        ),
    ]
