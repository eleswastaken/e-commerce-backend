# Generated by Django 4.1 on 2022-12-20 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_sku_skumapper_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='in_stock_amount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sold_amount',
        ),
        migrations.AddField(
            model_name='sku',
            name='in_stock',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='sku',
            name='slug',
            field=models.CharField(blank=True, max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(blank=True, max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='sku',
            name='barcode',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='sku',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sku',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]