# Generated by Django 2.2.12 on 2020-12-16 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0119_auto_20201216_1342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='date_addeds',
            new_name='date_added',
        ),
        migrations.AlterField(
            model_name='productrating',
            name='randomImageNumber',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='seller',
            name='followers',
            field=models.IntegerField(default=20630),
        ),
    ]
