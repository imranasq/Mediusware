# Generated by Django 4.0 on 2021-12-24 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20211101_0823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productvariantprice',
            name='price',
        ),
        migrations.RemoveField(
            model_name='productvariantprice',
            name='stock',
        ),
        migrations.AddField(
            model_name='productvariantprice',
            name='variant_one_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='productvariantprice',
            name='variant_one_stock',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='productvariantprice',
            name='variant_three_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='productvariantprice',
            name='variant_three_stock',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='productvariantprice',
            name='variant_two_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='productvariantprice',
            name='variant_two_stock',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='variant',
            name='color',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='variant',
            name='size',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
