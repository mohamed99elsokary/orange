# Generated by Django 4.0.4 on 2023-11-17 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_remove_customer_important_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='activation_date',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]