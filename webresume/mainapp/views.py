from django.shortcuts import render
from .models import *


def index(request):
    main_info = MainInfo.objects.filter(active_resume=True).last()
    personal_qualities = PersonalQualities.objects.filter(main_info=main_info.id)
    attainments = Attainments.objects.filter(main_info=main_info.id)
    contacts = Contacts.objects.filter(main_info=main_info.id)
    education = Education.objects.filter(main_info=main_info.id)
    projects = Projects.objects.filter(main_info=main_info.id)
    work_experience = WorkExperience.objects.filter(main_info=main_info.id)
    return render(request, 'mainapp/index.html', {'main_info': main_info,
                                                  'personal_qualities': personal_qualities,
                                                  'attainments': attainments,
                                                  'contacts': contacts,
                                                  'education': education,
                                                  'projects': projects,
                                                  'work_experience': work_experience})
