# Generated by Django 2.2.12 on 2020-12-02 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0037_auto_20201202_1318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
