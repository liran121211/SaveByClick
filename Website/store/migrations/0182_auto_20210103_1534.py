# Generated by Django 2.2.12 on 2021-01-03 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0181_auto_20210103_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(default='2F451FC2DEDB0ED3D9B7', max_length=50),
        ),
        migrations.AlterField(
            model_name='seller',
            name='followers',
            field=models.IntegerField(default=41370),
        ),
    ]