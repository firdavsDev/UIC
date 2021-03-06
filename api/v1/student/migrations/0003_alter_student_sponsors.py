# Generated by Django 4.0.4 on 2022-05-27 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0006_alter_sponsor_options'),
        ('student', '0002_student_allocated_amount_student_contract_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sponsors',
            field=models.ManyToManyField(blank=True, help_text='Homiylar', related_name='students_sponsors', to='sponsor.sponsor'),
        ),
    ]
