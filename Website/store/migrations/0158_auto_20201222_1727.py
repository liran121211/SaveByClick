# Generated by Django 2.2.12 on 2020-12-22 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0157_auto_20201220_2137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mainmessage',
            old_name='time',
            new_name='valid_till',
        ),
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(default='FD7C08549AA8A27C3DF0', max_length=50),
        ),
        migrations.AlterField(
            model_name='productrating',
            name='randomImageNumber',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='seller',
            name='followers',
            field=models.IntegerField(default=33163),
        ),
        migrations.AlterField(
            model_name='storerating',
            name='randomImageNumber',
            field=models.IntegerField(default=4),
        ),
    ]
