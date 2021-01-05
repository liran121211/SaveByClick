# Generated by Django 2.2.12 on 2020-12-14 20:25

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0091_productrating_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productrating',
            name='body_text',
            field=django_ckeditor_5.fields.CKEditor5Field(default='null', verbose_name='body_text'),
        ),
        migrations.AlterField(
            model_name='productrating',
            name='rating',
            field=models.CharField(default='1', max_length=100),
        ),
    ]