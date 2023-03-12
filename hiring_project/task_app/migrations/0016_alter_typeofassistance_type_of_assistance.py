# Generated by Django 4.1.7 on 2023-03-12 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0015_alter_district_district_name_alter_donor_donor_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeofassistance',
            name='type_of_assistance',
            field=models.CharField(choices=[('TA', 'TA'), ('Grant', 'Grant'), ('Loan', 'Loan')], max_length=6, unique=True),
        ),
    ]
