# Generated by Django 5.0.6 on 2024-06-13 08:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_customer_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumber',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer', verbose_name='مشتری'),
        ),
    ]