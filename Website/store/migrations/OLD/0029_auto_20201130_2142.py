# Generated by Django 2.2.12 on 2020-11-30 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_auto_20201130_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Seller'),
        ),
    ]
