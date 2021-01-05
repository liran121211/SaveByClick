# Generated by Django 2.2.12 on 2020-12-19 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0151_auto_20201219_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(default='23291E87DCEE2BCA912A', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='featured',
            field=models.CharField(default='Not Approved', max_length=20),
        ),
        migrations.AlterField(
            model_name='seller',
            name='followers',
            field=models.IntegerField(default=31827),
        ),
        migrations.AlterField(
            model_name='storerating',
            name='randomImageNumber',
            field=models.IntegerField(default=1),
        ),
    ]