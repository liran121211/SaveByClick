# Generated by Django 2.2.12 on 2020-12-16 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0116_auto_20201216_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='date_added',
            field=models.DateTimeField(default='2020-12-06 08:38:54.793849 +00:00'),
        ),
        migrations.AlterField(
            model_name='productrating',
            name='randomImageNumber',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='seller',
            name='followers',
            field=models.IntegerField(default=92583),
        ),
    ]