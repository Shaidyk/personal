# Generated by Django 3.0.8 on 2020-08-27 17:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0005_auto_20200827_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='amount',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
    ]
