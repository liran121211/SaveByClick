# Generated by Django 2.2.12 on 2020-12-03 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0043_auto_20201202_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('False', 'Not Active'), ('True', 'Active')], default='Enable', max_length=10),
        ),
    ]
