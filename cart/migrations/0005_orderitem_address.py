# Generated by Django 4.2.7 on 2023-11-25 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_discountcode_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
