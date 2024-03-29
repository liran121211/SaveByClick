# Generated by Django 2.2.12 on 2020-11-30 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_auto_20201129_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='User',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='Seller',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.Seller'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='User',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
