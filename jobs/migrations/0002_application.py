# Generated by Django 4.2.13 on 2024-06-08 14:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('date_of_birth', models.DateTimeField(verbose_name='Date Of Birth')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1,
                                            verbose_name='Gender')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('address', models.TextField(verbose_name='Address')),
                ('highest_education_level', models.CharField(
                    choices=[('NFE', 'No formal education'), ('PRI', 'Primary education'),
                             ('SEC', 'Secondary education'), ('VOC', 'Vocational training'),
                             ('BAC', "Bachelor's degree"), ('MAS', "Master's degree"), ('PHD', 'Doctorate or higher')],
                    max_length=3, verbose_name='Highest Level of Education')),
                ('school', models.CharField(max_length=100, verbose_name='School/University')),
                ('work_experience', models.TextField(verbose_name='Work Experience')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]