# Generated by Django 4.2.4 on 2023-09-17 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_sales_sale'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_banned',
        ),
    ]