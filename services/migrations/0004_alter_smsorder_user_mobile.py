# Generated by Django 3.2.12 on 2022-05-03 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20220503_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smsorder',
            name='user_mobile',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
