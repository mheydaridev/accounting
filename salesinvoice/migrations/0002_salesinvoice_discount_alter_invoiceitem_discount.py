# Generated by Django 5.0.6 on 2024-06-13 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesinvoice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesinvoice',
            name='discount',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='درصد تخفیف فاکتور'),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='discount',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='درصد تخفیف محصول'),
        ),
    ]