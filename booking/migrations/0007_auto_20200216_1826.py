# Generated by Django 3.0.3 on 2020-02-16 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_auto_20200216_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='price',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
