# Generated by Django 2.2.12 on 2020-12-17 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0139_auto_20201217_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(default='F0520D10E6187A12C85C', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='productrating',
            name='randomImageNumber',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='seller',
            name='followers',
            field=models.IntegerField(default=83491),
        ),
    ]
