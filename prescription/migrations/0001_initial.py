# Generated by Django 4.1.2 on 2023-03-22 17:15

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import prescription.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='active_Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ingredient name')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_in_a_week', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)])),
                ('date', models.DateField(default=datetime.date(2023, 3, 27))),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('allowed_number', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Clinical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinical_name', models.CharField(max_length=100, verbose_name='Clinical name')),
                ('clinical_location', models.CharField(max_length=255, verbose_name='Clinical location')),
                ('telephone', models.CharField(max_length=12, null=True)),
                ('phone', models.CharField(max_length=12, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.doctor')),
            ],
            options={
                'verbose_name': 'Clinical',
                'verbose_name_plural': 'Clinicals',
            },
        ),
        migrations.CreateModel(
            name='Interaction_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_created', models.DateField(default=datetime.datetime.now)),
                ('next_consultation', models.DateField(verbose_name='next consultation')),
                ('cancelation_date', models.DateField(null=True)),
                ('clinical', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Clinical', to='prescription.clinical')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='doctor_id', to='accounts.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_id', to='accounts.patient')),
            ],
            options={
                'verbose_name': 'Prescription',
                'verbose_name_plural': 'Prescriptions',
            },
        ),
        migrations.CreateModel(
            name='StandardMedicalAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Medical Analysis')),
                ('description', models.TextField(verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='StandardScreens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='screen name')),
                ('description', models.TextField(verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='TestScreen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.BinaryField(blank=True)),
                ('new', models.ImageField(blank=True, null=True, upload_to=prescription.models.image_upload)),
                ('file', models.FileField(blank=True, upload_to=prescription.models.image_upload)),
                ('file_path', models.FilePathField(blank=True)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StandardDrugs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Drug name')),
                ('desease', models.CharField(max_length=100, verbose_name='Desease name')),
                ('sideEffects', models.TextField(max_length=1000, verbose_name='Side Effects')),
                ('description', models.TextField(max_length=1000, verbose_name='Description')),
                ('drugType', models.CharField(max_length=100, null=True, verbose_name='Drug Type')),
                ('activeIngredient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prescription.active_ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField(null=True)),
                ('deadline', models.DateField()),
                ('is_done', models.BooleanField(default=False)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.patient')),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prescription.prescription')),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='StandardScreens', to='prescription.standardscreens')),
            ],
        ),
        migrations.CreateModel(
            name='PatientBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prescription.booking')),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.patient')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField(null=True)),
                ('deadline', models.DateField()),
                ('is_done', models.BooleanField(default=False)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.patient')),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prescription.prescription')),
                ('standard_medical_analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prescription.standardmedicalanalysis')),
            ],
        ),
        migrations.CreateModel(
            name='ingredient_interaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=1000, verbose_name='Description')),
                ('first', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='firstID', to='prescription.active_ingredient', verbose_name='First Active Ingredient ')),
                ('second', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secondID', to='prescription.active_ingredient', verbose_name='Second Active Ingredient ')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prescription.interaction_status')),
            ],
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_in', models.DateField(default=datetime.datetime.now, verbose_name='Start in')),
                ('end_in', models.DateField(verbose_name='End in')),
                ('dose_per_hour', models.FloatField(verbose_name='dose')),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='StandardDrugs', to='prescription.standarddrugs')),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prescription.prescription')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='clinical',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prescription.clinical'),
        ),
        migrations.AddField(
            model_name='booking',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.doctor'),
        ),
    ]
