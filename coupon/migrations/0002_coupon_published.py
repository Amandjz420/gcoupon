# Generated by Django 3.0.5 on 2020-04-24 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
