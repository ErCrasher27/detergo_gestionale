# Generated by Django 4.1.5 on 2023-01-08 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detergo_gestionale_app', '0005_remove_category_slug_remove_category_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='broughtitem',
            name='defect',
        ),
        migrations.AddField(
            model_name='broughtitem',
            name='notes',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ironing_price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='color',
            name='icon',
            field=models.ImageField(max_length=256, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='dry_price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='icon',
            field=models.ImageField(max_length=256, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='tailoring_price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='water_price',
            field=models.FloatField(null=True),
        ),
        migrations.DeleteModel(
            name='Defect',
        ),
    ]
