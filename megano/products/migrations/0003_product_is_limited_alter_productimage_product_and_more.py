# Generated by Django 4.2.4 on 2023-09-15 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_tovar"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_limited",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="productimage",
            name="product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="products.product",
            ),
        ),
        migrations.DeleteModel(
            name="Tovar",
        ),
    ]
