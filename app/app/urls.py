"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from SE import views

urlpatterns = [
    path('', views.home_page),
    path('admin/', admin.site.urls),
    path('conveniote/index', views.home_page, name='home'),
    path('conveniote/course1', views.course1, name='course1'),
    path('conveniote/video', views.video, name='video'),
    path('conveniote/grades', views.grades, name='grades'),
    path('conveniote/notes', views.notes, name='notes'),
    path('conveniote/syllabus', views.syllabus, name='syllabus'),
    path('conveniote/add_video_form_submssion/', views.add_video_form_submission, name = "addvideo"),
    path('conveniote/remove_video/', views.remove_video, name = "removevideo"),
    path('conveniote/assignment', views.assignment_form, name='assignment_form'),
    path('conveniote/evaluation', views.evaluation_form, name='evaluation_form')
]
