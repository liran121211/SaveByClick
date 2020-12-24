# Generated by Django 2.2.12 on 2020-12-22 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0159_auto_20201222_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotedproducts',
            name='unique_save',
            field=models.IntegerField(default=999),
        ),
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(default='830666A01224E052E794', max_length=50),
        ),
        migrations.AlterField(
            model_name='productrating',
            name='randomImageNumber',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='seller',
            name='followers',
            field=models.IntegerField(default=5243),
        ),
        migrations.AlterField(
            model_name='storerating',
            name='randomImageNumber',
            field=models.IntegerField(default=3),
        ),
    ]
