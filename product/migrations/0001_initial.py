# Generated by Django 4.2.4 on 2023-08-23 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('image', models.ImageField(upload_to='brands', verbose_name='Brand-Images-Upload')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
                ('flag', models.CharField(choices=[('Sale', 'Sale'), ('New', 'New'), ('Feature', 'Feature')], max_length=10, verbose_name='Flag')),
                ('image', models.ImageField(upload_to='image_psoduct', verbose_name='Image')),
                ('price', models.FloatField(verbose_name='Price')),
                ('sku', models.CharField(max_length=12, verbose_name='SKU')),
                ('subtitle', models.CharField(max_length=300, verbose_name='Subtitle')),
                ('dsecreiption', models.TextField(max_length=5000, verbose_name='Dsecreiption')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_brand', to='product.brand', verbose_name='Brands')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(verbose_name='Rate-Review')),
                ('review', models.CharField(max_length=500, verbose_name='Review')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created_at-Review')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_reviews', to='product.product', verbose_name='Product-Review')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_reviews', to=settings.AUTH_USER_MODEL, verbose_name='User-Review')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_image', verbose_name='Product-Images-Upload')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_image', to='product.product', verbose_name='Product-Images')),
            ],
        ),
    ]
