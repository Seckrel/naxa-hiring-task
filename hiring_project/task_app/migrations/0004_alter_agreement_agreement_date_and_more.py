# Generated by Django 4.1.7 on 2023-03-11 13:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0003_alter_project_agreement_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement',
            name='agreement_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='commitmentdisbursement',
            name='commitment',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='commitmentdisbursement',
            name='disbursement',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
