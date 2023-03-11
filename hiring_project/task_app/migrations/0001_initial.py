# Generated by Django 4.1.7 on 2023-03-11 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('agreement_id', models.AutoField(primary_key=True, serialize=False)),
                ('agreement_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CounterpartMinistry',
            fields=[
                ('counterpart_ministry_id', models.AutoField(primary_key=True, serialize=False)),
                ('counterpart_ministry_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('district_id', models.AutoField(primary_key=True, serialize=False)),
                ('district_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('donor_id', models.AutoField(primary_key=True, serialize=False)),
                ('donor_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ExecutingAgency',
            fields=[
                ('executing_agency_id', models.AutoField(primary_key=True, serialize=False)),
                ('executing_agency_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ImplementingPartner',
            fields=[
                ('implementing_partner_id', models.AutoField(primary_key=True, serialize=False)),
                ('implementing_partner_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('municipality_id', models.AutoField(primary_key=True, serialize=False)),
                ('municipality_name', models.CharField(max_length=255)),
                ('district_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.district')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_title', models.CharField(max_length=255)),
                ('project_status', models.CharField(max_length=255)),
                ('budget_type', models.CharField(choices=[('Off Budget', 'Off Budget'), ('On Budget', 'On Budget')], max_length=25)),
                ('humanitarian', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], max_length=3)),
                ('municipality_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.municipality')),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('province_id', models.AutoField(primary_key=True, serialize=False)),
                ('province_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('sector_id', models.AutoField(primary_key=True, serialize=False)),
                ('sector_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfAssistance',
            fields=[
                ('type_of_assistance_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_of_assistance', models.CharField(choices=[('TA', 'TA'), ('Grant', 'Grant'), ('Loan', 'Loan')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTypeOfAssistance',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.project')),
                ('type_of_assistance_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.typeofassistance')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectSector',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.project')),
                ('sector_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.sector')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImplementingPartner',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('implementing_partnet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.implementingpartner')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectExecutingAgency',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('executing_agency_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.executingagency')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.project')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.province'),
        ),
        migrations.CreateModel(
            name='CommitmentDisbursement',
            fields=[
                ('commitment_disbursement_id', models.AutoField(primary_key=True, serialize=False)),
                ('commitment', models.IntegerField()),
                ('disbursement', models.FloatField()),
                ('agreement_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.agreement')),
            ],
        ),
        migrations.AddField(
            model_name='agreement',
            name='donor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.donor'),
        ),
        migrations.AddField(
            model_name='agreement',
            name='executing_agency_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.executingagency'),
        ),
        migrations.AddField(
            model_name='agreement',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.project'),
        ),
        migrations.AddField(
            model_name='agreement',
            name='sector_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.sector'),
        ),
    ]
