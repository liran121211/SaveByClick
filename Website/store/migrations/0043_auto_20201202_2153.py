# Generated by Django 2.2.12 on 2020-12-02 21:53

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0042_productsss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=django_ckeditor_5.fields.CKEditor5Field(default='null', verbose_name='product_description'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Productsss',
        ),
    ]
