from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('projects_slider/', views.projects_slider, name='projects_slider'),
    path('project/<slug:slug_name>/', views.project, name='project'),
    path('send_email/', views.send_email, name='send_email')
]
