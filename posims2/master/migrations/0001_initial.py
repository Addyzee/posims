# Generated by Django 4.1.7 on 2023-04-02 18:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(max_length=300)),
                ('category', models.CharField(default='General', max_length=500)),
                ('description', models.TextField(blank=True, null=True)),
                ('count', models.FloatField(default=1)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.inventory')),
            ],
        ),
    ]
