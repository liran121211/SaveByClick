# Generated by Django 2.2.12 on 2020-12-14 22:56

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0094_productrating_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productrating',
            name='body_text',
        ),
        migrations.AddField(
            model_name='productrating',
            name='Description',
            field=django_ckeditor_5.fields.CKEditor5Field(default='null', verbose_name='Description'),
        ),
    ]
