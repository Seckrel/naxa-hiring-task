# Generated by Django 4.1.7 on 2023-03-12 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0011_project_counterpart_ministry_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='counterpart_ministry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='counterpart_ministry', to='task_app.counterpartministry'),
        ),
    ]
