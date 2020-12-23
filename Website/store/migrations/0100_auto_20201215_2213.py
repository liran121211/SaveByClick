# Generated by Django 2.2.12 on 2020-12-15 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0099_auto_20201215_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='productrating',
            name='randomImageNumber',
            field=models.FloatField(default=4),
        ),
        migrations.AlterField(
            model_name='seller',
            name='followers',
            field=models.IntegerField(default=14609),
        ),
        migrations.AlterField(
            model_name='storerating',
            name='randomImageNumber',
            field=models.FloatField(default=3),
        ),
    ]