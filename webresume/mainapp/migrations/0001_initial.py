# Generated by Django 4.1.5 on 2023-01-17 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='mainapp/images')),
                ('fio', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('marital_status', models.BooleanField()),
                ('busyness', models.CharField(max_length=50)),
                ('languages', models.CharField(max_length=100)),
                ('active_resume', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Основная информация',
                'verbose_name_plural': 'Основная информация',
            },
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=50)),
                ('set_up', models.DateField()),
                ('quit', models.DateField()),
                ('responsibility', models.TextField()),
                ('main_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.maininfo')),
            ],
            options={
                'verbose_name': 'Опыт работы',
                'verbose_name_plural': 'Опыт работы',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='mainapp/images')),
                ('description', models.TextField()),
                ('link', models.URLField()),
                ('main_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.maininfo')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='PersonalQualities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('main_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.maininfo')),
            ],
            options={
                'verbose_name': 'Качество',
                'verbose_name_plural': 'Качества',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=100)),
                ('education', models.CharField(max_length=50)),
                ('profession', models.CharField(max_length=100)),
                ('finish_date', models.DateField()),
                ('main_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.maininfo')),
            ],
            options={
                'verbose_name': 'Образование',
                'verbose_name_plural': 'Образование',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=100)),
                ('main_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.maininfo')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Attainments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('main_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.maininfo')),
            ],
            options={
                'verbose_name': 'Знание',
                'verbose_name_plural': 'Знания',
            },
        ),
    ]
