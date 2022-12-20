# Generated by Django 4.1 on 2022-12-19 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_alter_statuscode_code_alter_statuscode_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(editable=False)),
                ('last_modified', models.DateTimeField(editable=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariantOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(editable=False)),
                ('last_modified', models.DateTimeField(editable=False)),
                ('product_variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.productvariant')),
            ],
        ),
        migrations.CreateModel(
            name='Sku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('created_at', models.DateTimeField(editable=False)),
                ('last_modified', models.DateTimeField(editable=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariantOptionMapper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False)),
                ('last_modified', models.DateTimeField(editable=False)),
                ('product_variant_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.productvariantoption')),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.sku')),
            ],
        ),
    ]