# Generated by Django 4.2.13 on 2024-07-01 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t_app_product', '0007_auto_20240509_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='youtube_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
