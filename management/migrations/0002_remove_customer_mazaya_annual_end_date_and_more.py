# Generated by Django 4.1.1 on 2023-10-28 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("management", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="mazaya_annual_end_date",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="mazaya_annual_start_date",
        ),
        migrations.AddField(
            model_name="customer",
            name="User",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="customer",
            name="bills_payment",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="customer",
            name="important_notes",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="customer",
            name="is_important_notes",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="customer",
            name="is_net",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="customer",
            name="is_special",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="customer",
            name="notional_id",
            field=models.CharField(default="", max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="customer",
            name="smart_payment",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="customer",
            name="activation_date",
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="specialoffer",
            name="name",
            field=models.CharField(max_length=200),
        ),
    ]
