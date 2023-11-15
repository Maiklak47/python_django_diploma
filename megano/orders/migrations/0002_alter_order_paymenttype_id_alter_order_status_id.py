# Generated by Django 4.2.4 on 2023-09-07 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paymentType_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='orders.paymenttype'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='orders.status'),
        ),
    ]
