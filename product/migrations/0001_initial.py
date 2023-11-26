# Generated by Django 4.2.7 on 2023-11-20 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('percentage_discount', models.SmallIntegerField()),
                ('off_price', models.SmallIntegerField(null=True)),
                ('image', models.ImageField(upload_to='product/images')),
                ('color', models.ManyToManyField(related_name='products', to='product.color')),
                ('size', models.ManyToManyField(related_name='products', to='product.size')),
            ],
        ),
    ]