# Generated by Django 2.2.12 on 2020-11-29 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_auto_20201129_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
