# Generated by Django 2.2.12 on 2020-12-17 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0148_auto_20201217_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(default='A11FF5869D6948577E7B', max_length=50),
        ),
        migrations.AlterField(
            model_name='seller',
            name='followers',
            field=models.IntegerField(default=29542),
        ),
        migrations.AlterField(
            model_name='storerating',
            name='randomImageNumber',
            field=models.IntegerField(default=3),
        ),
    ]
