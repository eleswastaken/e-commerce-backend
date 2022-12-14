# Generated by Django 4.1 on 2022-12-11 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_cartitem_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='deleted_at',
        ),
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='sold_amount',
            field=models.IntegerField(default=0),
        ),
    ]
