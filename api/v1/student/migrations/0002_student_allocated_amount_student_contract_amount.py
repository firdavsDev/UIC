# Generated by Django 4.0.4 on 2022-05-25 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='allocated_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='student',
            name='contract_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
