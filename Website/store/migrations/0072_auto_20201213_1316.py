# Generated by Django 2.2.12 on 2020-12-13 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0071_auto_20201213_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactseller',
            name='receiver',
            field=models.IntegerField(),
        ),
    ]
