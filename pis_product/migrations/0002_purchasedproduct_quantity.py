# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-10 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pis_product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasedproduct',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=65),
        ),
    ]