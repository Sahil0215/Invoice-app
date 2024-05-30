# Generated by Django 5.0.6 on 2024-05-28 15:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_items_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_number', models.CharField(max_length=100)),
                ('bill_date', models.DateField()),
                ('total_quantity', models.CharField(max_length=10)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.buyer')),
                ('item', models.ManyToManyField(to='app.item')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.seller')),
            ],
        ),
    ]