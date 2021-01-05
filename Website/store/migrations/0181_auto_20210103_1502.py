# Generated by Django 2.2.12 on 2021-01-03 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0180_auto_20210103_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(default='21A00960D99733279590', max_length=50),
        ),
        migrations.AlterField(
            model_name='productrating',
            name='randomImageNumber',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='seller',
            name='followers',
            field=models.IntegerField(default=7872),
        ),
        migrations.AlterField(
            model_name='storerating',
            name='randomImageNumber',
            field=models.IntegerField(default=1),
        ),
    ]
