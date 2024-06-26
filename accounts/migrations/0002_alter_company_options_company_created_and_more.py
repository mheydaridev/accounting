# Generated by Django 5.0.6 on 2024-06-12 21:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'شرکت', 'verbose_name_plural': 'شرکت\u200cها'},
        ),
        migrations.AddField(
            model_name='company',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='زمان ثبت اطلاعات'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='زمان آخرین بروزرسانی اطلاعات'),
        ),
    ]
