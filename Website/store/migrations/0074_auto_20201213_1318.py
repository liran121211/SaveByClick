# Generated by Django 2.2.12 on 2020-12-13 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0073_auto_20201213_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactseller',
            name='receiver',
            field=models.IntegerField(default=1),
        ),
    ]
