# Generated by Django 2.2.12 on 2020-12-17 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0147_auto_20201217_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(default='2880445DB22C6C4849B4', max_length=50),
        ),
        migrations.AlterField(
            model_name='seller',
            name='followers',
            field=models.IntegerField(default=6280),
        ),
        migrations.AlterField(
            model_name='storerating',
            name='randomImageNumber',
            field=models.IntegerField(default=4),
        ),
    ]