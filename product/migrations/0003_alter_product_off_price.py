# Generated by Django 4.2.7 on 2023-11-20 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_published_product_slug_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='off_price',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
