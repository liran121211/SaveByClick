# Generated by Django 2.2.12 on 2020-12-14 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0085_contactsite'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactsite',
            name='image',
            field=models.ImageField(blank=True, default='null', null=True, upload_to=''),
        ),
    ]
