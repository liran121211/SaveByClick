# Generated by Django 2.2.12 on 2020-12-16 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0127_auto_20201216_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productrating',
            name='randomImageNumber',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='seller',
            name='followers',
            field=models.IntegerField(default=20462),
        ),
        migrations.AlterField(
            model_name='storerating',
            name='randomImageNumber',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='buyer',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='product',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Product'),
        ),
    ]
