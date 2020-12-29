# Generated by Django 2.2.12 on 2020-12-23 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0164_auto_20201222_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(default='CCDE3EDF2ECECFAAC405', max_length=50),
        ),
        migrations.AlterField(
            model_name='productrating',
            name='randomImageNumber',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='seller',
            name='followers',
            field=models.IntegerField(default=58831),
        ),
        migrations.AlterField(
            model_name='seller',
            name='store_name',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AlterField(
            model_name='storerating',
            name='randomImageNumber',
            field=models.IntegerField(default=1),
        ),
    ]
