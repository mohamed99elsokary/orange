# Generated by Django 4.0.4 on 2023-11-17 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_alter_customer_activation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='registration_date',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
