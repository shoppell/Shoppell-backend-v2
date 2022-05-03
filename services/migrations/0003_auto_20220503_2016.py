# Generated by Django 3.2.12 on 2022-05-03 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20220503_1739'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0002_auto_20220503_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='smsorder',
            name='to_users',
        ),
        migrations.AddField(
            model_name='smsorder',
            name='to_users',
            field=models.ManyToManyField(related_name='sms_receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='DailyShopView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view', models.PositiveIntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.shop')),
                ('user_ip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.ipaddress')),
            ],
        ),
        migrations.CreateModel(
            name='DailyProductView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view', models.PositiveIntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.product')),
                ('user_ip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.ipaddress')),
            ],
        ),
    ]
