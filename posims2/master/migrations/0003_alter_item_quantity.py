# Generated by Django 4.1.7 on 2023-04-09 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_item_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.CharField(default='1', max_length=200),
        ),
    ]