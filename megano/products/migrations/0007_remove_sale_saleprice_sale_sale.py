# Generated by Django 4.2.4 on 2023-09-15 10:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0006_product_sort_index_alter_product_tags"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sale",
            name="salePrice",
        ),
        migrations.AddField(
            model_name="sale",
            name="sale",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
