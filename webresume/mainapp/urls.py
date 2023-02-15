from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('project/<slug:slug_name>/', views.project, name='project'),
    path('send_email/', views.send_email, name='send_email')
]
