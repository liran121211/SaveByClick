# Generated by Django 2.2.12 on 2020-12-17 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0138_auto_20201217_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(default='A80FE911381CAE3D2FAE', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='productrating',
            name='randomImageNumber',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='seller',
            name='followers',
            field=models.IntegerField(default=85447),
        ),
        migrations.AlterField(
            model_name='storerating',
            name='randomImageNumber',
            field=models.IntegerField(default=2),
        ),
    ]
