# Generated by Django 4.0.4 on 2022-05-25 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0002_remove_sponsor_allocated_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]