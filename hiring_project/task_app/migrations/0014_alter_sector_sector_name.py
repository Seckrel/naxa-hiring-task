# Generated by Django 4.1.7 on 2023-03-12 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0013_alter_sector_sector_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sector',
            name='sector_name',
            field=models.CharField(max_length=255),
        ),
    ]
