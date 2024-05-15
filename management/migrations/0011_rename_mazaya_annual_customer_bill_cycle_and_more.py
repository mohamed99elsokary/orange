# Generated by Django 4.0.4 on 2024-05-15 00:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0010_alter_customer_account_manager_alter_customer_net_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='mazaya_annual',
            new_name='bill_cycle',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='registration_date',
            new_name='n_name',
        ),
        migrations.AlterField(
            model_name='customer',
            name='actual_bill',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='commission',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='online_payment',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.onlinepayment'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='special_offer',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='total_bill',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
