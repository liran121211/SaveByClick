# Generated by Django 2.2.12 on 2020-12-13 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0074_auto_20201213_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactseller',
            name='receiver',
            field=models.IntegerField(),
        ),
    ]
