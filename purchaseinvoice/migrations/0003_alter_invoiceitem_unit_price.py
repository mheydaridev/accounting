# Generated by Django 5.0.6 on 2024-06-13 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchaseinvoice', '0002_alter_invoiceitem_value_added_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceitem',
            name='unit_price',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=12, null=True, verbose_name='قیمت محصول'),
        ),
    ]
