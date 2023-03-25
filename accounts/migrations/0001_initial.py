# Generated by Django 4.1.2 on 2023-03-22 17:15

import accounts.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion

def create_initial_values(apps, schema_editor):
    UserType = apps.get_model('accounts', 'UserType')
    UserType.objects.create(typ=0, type_name='admin')
    UserType.objects.create(typ=1, type_name='patient')
    UserType.objects.create(typ=2, type_name='doctor')

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=30, null=True, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('typ', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=20, verbose_name='type name')),
            ],
        ),migrations.RunPython(create_initial_values),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_birth', models.DateField(null=True)),
                ('phone', models.CharField(max_length=11, validators=[accounts.models.phoneValidate])),
                ('city', models.CharField(choices=[('Cairo', 'Cairo'), ('Alexandria', 'Alexandria'), ('Giza', 'Giza'), ('Shubra El Kheima', 'Shubra El Kheima'), ('Port Said', 'Port Said'), ('Suez', 'Suez'), ('El Mahalla El Kubra', 'El Mahalla El Kubra'), ('Luxor', 'Luxor'), ('Mansoura', 'Mansoura'), ('Tanta', 'Tanta'), ('Asyut', 'Asyut'), ('Ismailia', 'Ismailia'), ('Faiyum', 'Faiyum'), ('Zagazig', 'Zagazig'), ('Damietta', 'Damietta'), ('Aswan', 'Aswan'), ('Minya', 'Minya'), ('Damanhur', 'Damanhur'), ('Beni Suef', 'Beni Suef'), ('Hurghada', 'Hurghada'), ('Qena', 'Qena'), ('Sohag', 'Sohag'), ('Shibin El Kom', 'Shibin El Kom'), ('Banha', 'Banha'), ('Arish', 'Arish'), ('Qalyubia', 'Qalyubia'), ('Gharbia', 'Gharbia')], max_length=30)),
                ('avatar', models.TextField(blank=True)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1)),
            ],
            options={
                'verbose_name': 'Admin',
                'verbose_name_plural': 'Admins',
            },
            bases=('accounts.user', models.Model),
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_birth', models.DateField(null=True)),
                ('phone', models.CharField(max_length=11, validators=[accounts.models.phoneValidate])),
                ('city', models.CharField(choices=[('Cairo', 'Cairo'), ('Alexandria', 'Alexandria'), ('Giza', 'Giza'), ('Shubra El Kheima', 'Shubra El Kheima'), ('Port Said', 'Port Said'), ('Suez', 'Suez'), ('El Mahalla El Kubra', 'El Mahalla El Kubra'), ('Luxor', 'Luxor'), ('Mansoura', 'Mansoura'), ('Tanta', 'Tanta'), ('Asyut', 'Asyut'), ('Ismailia', 'Ismailia'), ('Faiyum', 'Faiyum'), ('Zagazig', 'Zagazig'), ('Damietta', 'Damietta'), ('Aswan', 'Aswan'), ('Minya', 'Minya'), ('Damanhur', 'Damanhur'), ('Beni Suef', 'Beni Suef'), ('Hurghada', 'Hurghada'), ('Qena', 'Qena'), ('Sohag', 'Sohag'), ('Shibin El Kom', 'Shibin El Kom'), ('Banha', 'Banha'), ('Arish', 'Arish'), ('Qalyubia', 'Qalyubia'), ('Gharbia', 'Gharbia')], max_length=30)),
                ('avatar', models.TextField(blank=True)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1)),
                ('price', models.PositiveIntegerField(default=0)),
                ('bio', models.CharField(blank=True, max_length=100, null=True)),
                ('about', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Doctor',
                'verbose_name_plural': 'Doctors',
            },
            bases=('accounts.user', models.Model),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_birth', models.DateField(null=True)),
                ('phone', models.CharField(max_length=11, validators=[accounts.models.phoneValidate])),
                ('city', models.CharField(choices=[('Cairo', 'Cairo'), ('Alexandria', 'Alexandria'), ('Giza', 'Giza'), ('Shubra El Kheima', 'Shubra El Kheima'), ('Port Said', 'Port Said'), ('Suez', 'Suez'), ('El Mahalla El Kubra', 'El Mahalla El Kubra'), ('Luxor', 'Luxor'), ('Mansoura', 'Mansoura'), ('Tanta', 'Tanta'), ('Asyut', 'Asyut'), ('Ismailia', 'Ismailia'), ('Faiyum', 'Faiyum'), ('Zagazig', 'Zagazig'), ('Damietta', 'Damietta'), ('Aswan', 'Aswan'), ('Minya', 'Minya'), ('Damanhur', 'Damanhur'), ('Beni Suef', 'Beni Suef'), ('Hurghada', 'Hurghada'), ('Qena', 'Qena'), ('Sohag', 'Sohag'), ('Shibin El Kom', 'Shibin El Kom'), ('Banha', 'Banha'), ('Arish', 'Arish'), ('Qalyubia', 'Qalyubia'), ('Gharbia', 'Gharbia')], max_length=30)),
                ('avatar', models.TextField(blank=True)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1)),
                ('doctor_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.doctor', verbose_name='Doctor_id')),
            ],
            options={
                'verbose_name': 'Patient',
                'verbose_name_plural': 'Patients',
            },
            bases=('accounts.user', models.Model),
        ),
        migrations.AddField(
            model_name='user',
            name='typ',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.usertype'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('feedback', models.TextField(blank=True, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.patient')),
            ],
            options={
                'unique_together': {('doctor', 'patient')},
                'index_together': {('doctor', 'patient')},
            },
        ),
    ]
