# Generated by Django 2.2.12 on 2020-12-02 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0033_auto_20201202_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lastlogin',
            name='logout',
        ),
    ]