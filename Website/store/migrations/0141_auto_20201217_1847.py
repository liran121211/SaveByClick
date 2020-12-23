# Generated by Django 2.2.12 on 2020-12-17 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0140_auto_20201217_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(default='DCCE46E3850C5DFBF9C5', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='productrating',
            name='randomImageNumber',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='seller',
            name='followers',
            field=models.IntegerField(default=33848),
        ),
        migrations.AlterField(
            model_name='storerating',
            name='randomImageNumber',
            field=models.IntegerField(default=1),
        ),
    ]