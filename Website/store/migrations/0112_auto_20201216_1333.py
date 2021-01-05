# Generated by Django 2.2.12 on 2020-12-16 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0111_auto_20201216_1241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='Buyer',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='image',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='price',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='store_name',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wishlist',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='productrating',
            name='randomImageNumber',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='seller',
            name='followers',
            field=models.IntegerField(default=43085),
        ),
        migrations.AlterField(
            model_name='storerating',
            name='randomImageNumber',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Product'),
        ),
    ]
