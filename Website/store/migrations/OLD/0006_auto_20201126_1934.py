# Generated by Django 2.2.12 on 2020-11-26 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20201126_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.CharField(default=66920, max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productss',
            name='id',
            field=models.CharField(default=25858, max_length=10, primary_key=True, serialize=False),
        ),
    ]
