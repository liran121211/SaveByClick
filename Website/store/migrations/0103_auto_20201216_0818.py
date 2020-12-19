# Generated by Django 2.2.12 on 2020-12-16 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0102_auto_20201215_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productrating',
            name='image',
        ),
        migrations.AlterField(
            model_name='productrating',
            name='randomImageNumber',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='seller',
            name='followers',
            field=models.IntegerField(default=63916),
        ),
        migrations.AlterField(
            model_name='storerating',
            name='randomImageNumber',
            field=models.IntegerField(default=2),
        ),
    ]
