# Generated by Django 4.2.7 on 2023-11-11 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='token',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
