# Generated by Django 4.1.5 on 2023-02-14 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Busyness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('busyness', models.CharField(max_length=50, verbose_name='Занятось')),
            ],
            options={
                'verbose_name': 'Занятость',
                'verbose_name_plural': 'Занятость',
            },
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50, verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='MainInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images/mainapp', verbose_name='Фото')),
                ('fio', models.CharField(max_length=100, verbose_name='ФИО')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
                ('marital_status', models.BooleanField(verbose_name='Семейное положение')),
                ('active_resume', models.BooleanField(verbose_name='Активность резюме')),
                ('busyness', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.busyness', verbose_name='Занятость')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.cities', verbose_name='Город')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.countries', verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Основная информация',
                'verbose_name_plural': 'Основная информация',
            },
        ),
        migrations.CreateModel(
            name='Professions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=100, verbose_name='Профессия')),
            ],
            options={
                'verbose_name': 'Профессия',
                'verbose_name_plural': 'Профессии',
            },
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100, verbose_name='Должность')),
                ('company', models.CharField(max_length=50, verbose_name='Компания')),
                ('set_up', models.DateField(verbose_name='Дата устроиства')),
                ('quit', models.DateField(verbose_name='Дата увольнения')),
                ('responsibility', models.TextField(verbose_name='Обязанности')),
                ('main_info', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.maininfo', verbose_name='Резюме')),
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
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Ссылка')),
                ('project', models.CharField(max_length=100, verbose_name='Проект')),
                ('image', models.ImageField(upload_to='images/mainapp', verbose_name='Фото')),
                ('description', models.TextField(verbose_name='Описание')),
                ('link', models.URLField(verbose_name='Cсылка на GitHub')),
                ('main_info', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.maininfo', verbose_name='Резюме')),
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
                ('quality', models.CharField(max_length=50, verbose_name='Качество')),
                ('main_info', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.maininfo', verbose_name='Резюме')),
            ],
            options={
                'verbose_name': 'Качество',
                'verbose_name_plural': 'Качества',
            },
        ),
        migrations.AddField(
            model_name='maininfo',
            name='profession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.professions', verbose_name='Профессия'),
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=100, verbose_name='Иностранный язык')),
                ('main_info', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.maininfo', verbose_name='Резюме')),
            ],
            options={
                'verbose_name': 'Иностранный язык',
                'verbose_name_plural': 'Иностранные языки',
            },
        ),
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('knowledge', models.CharField(max_length=100, verbose_name='Знание')),
                ('main_info', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.maininfo', verbose_name='Резюме')),
            ],
            options={
                'verbose_name': 'Знание',
                'verbose_name_plural': 'Знания',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=100, verbose_name='Заведение')),
                ('education', models.CharField(max_length=50, verbose_name='Образование')),
                ('profession', models.CharField(max_length=100, verbose_name='Профессия')),
                ('finish_date', models.DateField(verbose_name='Дата окончания')),
                ('main_info', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.maininfo', verbose_name='Резюме')),
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
                ('contact', models.CharField(max_length=50, verbose_name='Контакт')),
                ('value', models.CharField(max_length=100, verbose_name='Значение')),
                ('main_info', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.maininfo', verbose_name='Резюме')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]
