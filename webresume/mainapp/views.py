from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from .models import *
from .forms import *

main_info = None
projects = None


def index(request):
    global main_info
    main_info = MainInfo.objects.filter(active_resume=True).last()
    email_form = EmailForm()
    resume_data = {'main_info': None}
    if main_info:
        global projects
        projects = Projects.objects.filter(main_info=main_info.pk)
        resume_data = {
            'main_info': main_info,
            'knowledge': Knowledge.objects.filter(main_info=main_info.pk),
            'languages': Languages.objects.filter(main_info=main_info.pk),
            'qualities': PersonalQualities.objects.filter(main_info=main_info.pk),
            'contacts': Contacts.objects.filter(main_info=main_info.pk),
            'education': Education.objects.filter(main_info=main_info.pk),
            'projects': projects.first(),
            'count_projects': projects.count(),
            'work_experience': WorkExperience.objects.filter(main_info=main_info.pk),
            'email_form': email_form
        }
    return render(request, 'mainapp/resume.html', context=resume_data)


def projects_slider(request):
    index = int(request.GET.get('index'))
    return JsonResponse({
                            'slug': projects[index].get_absolute_url(),
                            'project': projects[index].project,
                            'image': projects[index].image.url
                        })


def project(request, slug_name):
    project = Projects.objects.get(slug=slug_name)
    return render(request, 'mainapp/project.html', {'project': project})


def send_email(request):
    if request.method == 'POST':
        if EmailForm(request.POST).is_valid():
            message = request.POST.get('message')
            send_mail(
                'Резюме',
                message,
                'kirillbobrowsky_resume@mail.ru',
                ['kirillbobrowsky_resume@mail.ru'],
                fail_silently=False,
            )
            return JsonResponse({'is_send': True})
        else:
            return JsonResponse({'is_send': False})
