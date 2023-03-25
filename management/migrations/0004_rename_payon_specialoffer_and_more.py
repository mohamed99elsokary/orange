# Generated by Django 4.0.4 on 2023-03-25 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_customer_activation_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Payon',
            new_name='SpecialOffer',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='mr',
            new_name='mr_to_account',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='pay_on',
            new_name='special_offer',
        ),
        migrations.AddField(
            model_name='customer',
            name='lines_to_same_user',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='mr_to_corporate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='new_line',
            field=models.BooleanField(default=False),
        ),
    ]
