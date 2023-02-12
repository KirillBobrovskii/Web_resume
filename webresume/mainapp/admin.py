from django.contrib import admin
from .models import *


class ProfessionsAdmin(admin.ModelAdmin):
    search_fields = ('profession',)


admin.site.register(Professions, ProfessionsAdmin)


class CountriesAdmin(admin.ModelAdmin):
    search_fields = ('country',)


admin.site.register(Countries, CountriesAdmin)


class CitiesAdmin(admin.ModelAdmin):
    search_fields = ('city',)


admin.site.register(Cities, CitiesAdmin)


class BusynessAdmin(admin.ModelAdmin):
    search_fields = ('busyness',)


admin.site.register(Busyness, BusynessAdmin)


class MainInfoAdmin(admin.ModelAdmin):
    list_display = ('profession', 'photo', 'fio', 'birthday', 'country', 'city', 'marital_status', 'busyness',
                    'active_resume')
    search_fields = ('fio',)


admin.site.register(MainInfo, MainInfoAdmin)


class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('main_info', 'language')
    search_fields = ('main_info__fio',)


admin.site.register(Languages, LanguagesAdmin)


class KnowledgeAdmin(admin.ModelAdmin):
    list_display = ('main_info', 'knowledge')
    search_fields = ('main_info__fio',)


admin.site.register(Knowledge, KnowledgeAdmin)


class PersonalQualitiesAdmin(admin.ModelAdmin):
    list_display = ('main_info', 'quality')
    search_fields = ('main_info__fio',)


admin.site.register(PersonalQualities, PersonalQualitiesAdmin)


class EducationAdmin(admin.ModelAdmin):
    list_display = ('main_info', 'institution', 'education', 'profession', 'finish_date')
    search_fields = ('main_info__fio',)


admin.site.register(Education, EducationAdmin)


class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('main_info', 'position', 'company', 'set_up', 'quit', 'responsibility')
    search_fields = ('main_info__fio',)


admin.site.register(WorkExperience, WorkExperienceAdmin)


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('main_info', 'project', 'image', 'description', 'link')
    search_fields = ('main_info__fio',)


admin.site.register(Projects, ProjectsAdmin)


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('main_info', 'contact', 'value')
    search_fields = ('main_info__fio',)


admin.site.register(Contacts, ContactsAdmin)
