# Generated by Django 2.2.12 on 2020-12-09 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0062_contactseller_read_or_not'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactbuyer',
            name='read_or_not',
            field=models.BooleanField(default=False),
        ),
    ]
