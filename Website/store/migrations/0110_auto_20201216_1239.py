# Generated by Django 2.2.12 on 2020-12-16 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0109_auto_20201216_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='product',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Product'),
        ),
        migrations.AlterField(
            model_name='productrating',
            name='randomImageNumber',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='seller',
            name='followers',
            field=models.IntegerField(default=63669),
        ),
        migrations.AlterField(
            model_name='storerating',
            name='randomImageNumber',
            field=models.IntegerField(default=1),
        ),
    ]
