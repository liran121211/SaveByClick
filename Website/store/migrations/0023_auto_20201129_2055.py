# Generated by Django 2.2.12 on 2020-11-29 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_auto_20201126_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.CharField(default=79644, max_length=10, primary_key=True, serialize=False),
        ),
    ]
