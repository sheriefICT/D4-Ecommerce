# Generated by Django 4.2.4 on 2023-09-30 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_code_alter_orderdetail_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='X7FWYY80', max_length=10),
        ),
    ]