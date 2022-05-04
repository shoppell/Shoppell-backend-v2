# Generated by Django 3.2.12 on 2022-05-04 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_user_is_ban'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_shop_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_shop_owner',
            field=models.BooleanField(default=False),
        ),
    ]
