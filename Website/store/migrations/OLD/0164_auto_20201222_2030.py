# Generated by Django 2.2.12 on 2020-12-22 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0163_auto_20201222_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='productrating',
            name='image',
            field=models.ImageField(blank=True, default='null', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(default='AA903AC4E3CC6EECA4F0', max_length=50),
        ),
        migrations.AlterField(
            model_name='productrating',
            name='randomImageNumber',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='seller',
            name='followers',
            field=models.IntegerField(default=95068),
        ),
        migrations.AlterField(
            model_name='storerating',
            name='randomImageNumber',
            field=models.IntegerField(default=4),
        ),
    ]
