# Generated by Django 2.2.12 on 2020-11-26 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20201126_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.CharField(default=47331, max_length=10, primary_key=True, serialize=False),
        ),
    ]
