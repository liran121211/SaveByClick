# Generated by Django 2.2.12 on 2020-12-13 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0070_wishlist_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactseller',
            name='receiver',
            field=models.IntegerField(default=0),
        ),
    ]