# Generated by Django 4.0.4 on 2023-03-25 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_rename_payon_specialoffer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='special_offer',
        ),
        migrations.DeleteModel(
            name='SpecialOffer',
        ),
    ]
