# Generated by Django 2.2.12 on 2020-12-14 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0088_auto_20201214_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactsite',
            name='priority',
        ),
    ]
