from django.db import models


class Professions(models.Model):
    profession = models.CharField(max_length=100, verbose_name='Профессия')

    def __str__(self):
        return self.profession

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'


class Countries(models.Model):
    country = models.CharField(max_length=50, verbose_name='Страна')

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Cities(models.Model):
    city = models.CharField(max_length=50, verbose_name='Город')

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Busyness(models.Model):
    busyness = models.CharField(max_length=50, verbose_name='Занятось')

    def __str__(self):
        return self.busyness

    class Meta:
        verbose_name = 'Занятость'
        verbose_name_plural = 'Занятость'


class MainInfo(models.Model):
    profession = models.ForeignKey(Professions, on_delete=models.PROTECT, verbose_name='Профессия')
    photo = models.ImageField(upload_to='images/mainapp', verbose_name='Фото')
    fio = models.CharField(max_length=100, verbose_name='ФИО')
    birthday = models.DateField(verbose_name='Дата рождения')
    country = models.ForeignKey(Countries, on_delete=models.PROTECT, verbose_name='Страна')
    city = models.ForeignKey(Cities, on_delete=models.PROTECT, verbose_name='Город')
    marital_status = models.BooleanField(verbose_name='Семейное положение')
    busyness = models.ForeignKey(Busyness, on_delete=models.PROTECT, verbose_name='Занятость')
    active_resume = models.BooleanField(verbose_name='Активность резюме')

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Основная информация'
        verbose_name_plural = 'Основная информация'


class Languages(models.Model):
    main_info = models.ForeignKey(MainInfo, on_delete=models.PROTECT, verbose_name='Резюме')
    language = models.CharField(max_length=100, verbose_name='Иностранный язык')

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = 'Иностранный язык'
        verbose_name_plural = 'Иностранные языки'


class Knowledge(models.Model):
    main_info = models.ForeignKey(MainInfo, on_delete=models.PROTECT, verbose_name='Резюме')
    knowledge = models.CharField(max_length=100, verbose_name='Знание')

    def __str__(self):
        return self.knowledge

    class Meta:
        verbose_name = 'Знание'
        verbose_name_plural = 'Знания'


class PersonalQualities(models.Model):
    main_info = models.ForeignKey(MainInfo, on_delete=models.PROTECT, verbose_name='Резюме')
    quality = models.CharField(max_length=50, verbose_name='Качество')

    def __str__(self):
        return self.quality

    class Meta:
        verbose_name = 'Качество'
        verbose_name_plural = 'Качества'


class Education(models.Model):
    main_info = models.ForeignKey(MainInfo, on_delete=models.PROTECT, verbose_name='Резюме')
    institution = models.CharField(max_length=100, verbose_name='Заведение')
    education = models.CharField(max_length=50, verbose_name='Образование')
    profession = models.CharField(max_length=100, verbose_name='Профессия')
    finish_date = models.DateField(verbose_name='Дата окончания')

    def __str__(self):
        return self.institution

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'


class WorkExperience(models.Model):
    main_info = models.ForeignKey(MainInfo, on_delete=models.PROTECT, verbose_name='Резюме')
    position = models.CharField(max_length=100, verbose_name='Должность')
    company = models.CharField(max_length=50, verbose_name='Компания')
    set_up = models.DateField(verbose_name='Дата устроиства')
    quit = models.DateField(verbose_name='Дата увольнения')
    responsibility = models.TextField(verbose_name='Обязанности')

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'


class Projects(models.Model):
    main_info = models.ForeignKey(MainInfo, on_delete=models.PROTECT, verbose_name='Резюме')
    project = models.CharField(max_length=100, verbose_name='Проект')
    image = models.ImageField(upload_to='images/mainapp', verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')
    link = models.URLField(verbose_name='Ссылка')

    def __str__(self):
        return self.project

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Contacts(models.Model):
    main_info = models.ForeignKey(MainInfo, on_delete=models.PROTECT, verbose_name='Резюме')
    contact = models.CharField(max_length=50, verbose_name='Контакт')
    value = models.CharField(max_length=100, verbose_name='Значение')

    def __str__(self):
        return self.contact

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
