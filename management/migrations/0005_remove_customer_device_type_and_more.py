# Generated by Django 4.0.4 on 2023-11-17 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_alter_customer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='device_type',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='installments_end_date',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='installments_phone_number',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='installments_start_date',
        ),
        migrations.AlterField(
            model_name='customer',
            name='bills_payment',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='notional_id',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
