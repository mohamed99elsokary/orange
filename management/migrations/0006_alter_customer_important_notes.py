# Generated by Django 4.0.4 on 2023-11-17 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_remove_customer_device_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='important_notes',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]