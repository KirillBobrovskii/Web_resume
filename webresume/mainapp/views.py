from django.shortcuts import render
from .models import *
from .forms import *


def index(request):
    main_info = MainInfo.objects.filter(active_resume=True).last()
    email_form = EmailForm()
    resume_data = {'main_info': None}
    if main_info:
        resume_data = {
            'main_info': main_info,
            'knowledge': Knowledge.objects.filter(main_info=main_info.pk),
            'languages': Languages.objects.filter(main_info=main_info.pk),
            'qualities': PersonalQualities.objects.filter(main_info=main_info.pk),
            'contacts': Contacts.objects.filter(main_info=main_info.pk),
            'education': Education.objects.filter(main_info=main_info.pk),
            'projects': Projects.objects.filter(id=1, main_info=main_info.pk),
            'projects_count': Projects.objects.filter(main_info=main_info.pk).count(),
            'work_experience': WorkExperience.objects.filter(main_info=main_info.pk),
            'email_form': email_form
        }
    return render(request, 'mainapp/resume.html', context=resume_data)


def send_email(request):
    #email_form = EmailForm(request.POST)
    #if email_form.is_valid():
        # message = request.POST.get('message')
        # send_mail(
        #     'Резюме',
        #     message,
        #     'kirillbobrowsky_resume@mail.ru',
        #     ['kirillbobrowsky_resume@mail.ru'],
        #     fail_silently=False,
        # )
    #else:
        #return HttpResponse('Invalid data')
    return render(request, 'mainapp/send_email.html')
