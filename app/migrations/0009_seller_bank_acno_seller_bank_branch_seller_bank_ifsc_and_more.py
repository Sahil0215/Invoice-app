# Generated by Django 5.0.6 on 2024-05-29 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_buyer_b_city_buyer_b_pincode_buyer_b_state_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='bank_acno',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='seller',
            name='bank_branch',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='seller',
            name='bank_ifsc',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='seller',
            name='bank_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
