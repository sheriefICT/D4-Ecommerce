# Generated by Django 4.2.4 on 2023-09-11 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slag',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
