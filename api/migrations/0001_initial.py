# Generated by Django 4.2.11 on 2024-05-09 21:55

import api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='default_product_image.jpg', upload_to=api.models.image_path)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('important', models.BooleanField(default=False)),
                ('img1', models.ImageField(default='default_product_image.jpg', upload_to=api.models.image_path)),
                ('img2', models.ImageField(default='default_product_image.jpg', upload_to=api.models.image_path)),
                ('img3', models.ImageField(default='default_product_image.jpg', upload_to=api.models.image_path)),
                ('img4', models.ImageField(default='default_product_image.jpg', upload_to=api.models.image_path)),
                ('img5', models.ImageField(default='default_product_image.jpg', upload_to=api.models.image_path)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='api_products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]