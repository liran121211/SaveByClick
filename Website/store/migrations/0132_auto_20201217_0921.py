# Generated by Django 2.2.12 on 2020-12-17 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0131_auto_20201217_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pickup',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='productrating',
            name='randomImageNumber',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='seller',
            name='followers',
            field=models.IntegerField(default=80843),
        ),
        migrations.AlterField(
            model_name='storerating',
            name='randomImageNumber',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transactions_id',
            field=models.IntegerField(default=98054332),
        ),
    ]