# Generated by Django 4.1.7 on 2023-03-12 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0012_alter_project_counterpart_ministry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sector',
            name='sector_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
