# Generated by Django 3.0.8 on 2020-11-13 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_products',
            field=models.CharField(default=0, max_length=500),
        ),
    ]
