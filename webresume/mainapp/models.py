from django.db import models


class MainInfo(models.Model):
    profession = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="mainapp/images")
    fio = models.CharField(max_length=100)
    birthday = models.DateField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    marital_status = models.BooleanField()
    busyness = models.CharField(max_length=50)
    languages = models.CharField(max_length=100)
    active_resume = models.BooleanField()

    class Meta:
        verbose_name = 'Основная информация'
        verbose_name_plural = 'Основная информация'


class Attainments(models.Model):
    main_info = models.ForeignKey(MainInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Знание'
        verbose_name_plural = 'Знания'


class PersonalQualities(models.Model):
    main_info = models.ForeignKey(MainInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Качество'
        verbose_name_plural = 'Качества'


class Education(models.Model):
    main_info = models.ForeignKey(MainInfo, on_delete=models.CASCADE)
    institution = models.CharField(max_length=100)
    education = models.CharField(max_length=50)
    profession = models.CharField(max_length=100)
    finish_date = models.DateField()

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'


class WorkExperience(models.Model):
    main_info = models.ForeignKey(MainInfo, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=50)
    set_up = models.DateField()
    quit = models.DateField()
    responsibility = models.TextField()

    class Meta:
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'


class Projects(models.Model):
    main_info = models.ForeignKey(MainInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="mainapp/images")
    description = models.TextField()
    link = models.URLField()

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Contacts(models.Model):
    main_info = models.ForeignKey(MainInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
