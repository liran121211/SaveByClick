# Generated by Django 2.2.12 on 2020-11-26 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_auto_20201126_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.CharField(default=35784, max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='shippingadd',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
