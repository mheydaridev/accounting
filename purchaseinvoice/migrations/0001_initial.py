# Generated by Django 5.0.6 on 2024-06-12 20:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('supplier', '0001_initial'),
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_date', models.DateField(verbose_name='تاریخ فاکتور')),
                ('value_added', models.PositiveIntegerField(blank=True, null=True, verbose_name='درصد ارزش افزوده برای همه محصولات')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='زمان ثبت اطلاعات')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='زمان آخرین بروزرسانی اطلاعات')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier', verbose_name='تأمین کننده')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.warehouse', verbose_name='انبار')),
            ],
            options={
                'verbose_name': 'فاکتور خرید',
                'verbose_name_plural': 'فاکتورهای خرید',
            },
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='تعداد')),
                ('unit_price', models.DecimalField(decimal_places=0, max_digits=12, verbose_name='قیمت محصول')),
                ('value_added', models.PositiveIntegerField(blank=True, null=True, verbose_name='درصد ارزش افزوده برای این محصول')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_invoice_items', to='product.product', verbose_name='محصول')),
                ('purchase_invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchaseinvoice.purchaseinvoice', verbose_name='فاکتور خرید')),
            ],
            options={
                'verbose_name': 'آیتم فاکتور',
                'verbose_name_plural': 'آیتم\u200cهای فاکتور',
            },
        ),
    ]
