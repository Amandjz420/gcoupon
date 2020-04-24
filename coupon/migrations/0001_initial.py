# Generated by Django 3.0.5 on 2020-04-24 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_category', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('cat_number', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_merchant', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('merchant_number', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=80, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('coupon_number', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('active', 'ACTIVE'), ('inactive', 'INACTIVE')], default='active', max_length=25)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=250, null=True)),
                ('restriction', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.CharField(blank=True, max_length=200, null=True)),
                ('code', models.CharField(blank=True, max_length=100, null=True)),
                ('network', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(blank=True, null=True, to='coupon.Category')),
                ('desc_updated', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('merchant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='coupon.Merchant')),
                ('type', models.ManyToManyField(blank=True, null=True, to='coupon.Type')),
            ],
            options={
                'ordering': ['-rating'],
            },
        ),
    ]
