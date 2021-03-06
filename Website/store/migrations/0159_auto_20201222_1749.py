# Generated by Django 2.2.12 on 2020-12-22 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0158_auto_20201222_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(default='7E512F26BA718802E6C1', max_length=50),
        ),
        migrations.AlterField(
            model_name='productrating',
            name='randomImageNumber',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='seller',
            name='followers',
            field=models.IntegerField(default=42450),
        ),
        migrations.AlterField(
            model_name='storerating',
            name='randomImageNumber',
            field=models.IntegerField(default=2),
        ),
        migrations.CreateModel(
            name='PromotedProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.CharField(max_length=10)),
                ('banner_image', models.ImageField(blank=True, default='null', null=True, upload_to='')),
                ('slideshow', models.CharField(max_length=10)),
                ('slideshow_image', models.ImageField(blank=True, default='null', null=True, upload_to='')),
                ('popup', models.CharField(max_length=10)),
                ('popup_image', models.ImageField(blank=True, default='null', null=True, upload_to='')),
                ('product_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.Product')),
            ],
        ),
    ]
