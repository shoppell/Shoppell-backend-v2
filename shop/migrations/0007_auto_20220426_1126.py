# Generated by Django 2.2.28 on 2022-04-26 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_product_product_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_images',
        ),
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(default=1, upload_to='products'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
        migrations.AddField(
            model_name='product',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
        migrations.AddField(
            model_name='product',
            name='image6',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
