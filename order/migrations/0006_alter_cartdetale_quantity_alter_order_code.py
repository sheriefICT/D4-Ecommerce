# Generated by Django 4.2.4 on 2023-10-01 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdetale',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='1B34X2UU', max_length=10),
        ),
    ]
