# Generated by Django 3.2.12 on 2022-05-11 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_shop_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='image',
            field=models.ImageField(default=1, upload_to='shops'),
            preserve_default=False,
        ),
    ]
