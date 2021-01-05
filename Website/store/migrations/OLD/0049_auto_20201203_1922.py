# Generated by Django 2.2.12 on 2020-12-03 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0048_product_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='photo',
        ),
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(blank=True, default='null', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, default='null', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, default='null', null=True, upload_to=''),
        ),
    ]
