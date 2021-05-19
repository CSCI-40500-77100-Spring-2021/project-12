from django.contrib import admin
from django.urls import path
from SE import views

urlpatterns = [
    path('', views.home_page),
    path('admin/', admin.site.urls),
    path('conveniote/index', views.home_page, name='home'),
    path('conveniote/home', views.front_page, name='front'),
    path('conveniote/course1', views.course1, name='course1'),
    path('conveniote/video', views.video, name='video'),
    path('conveniote/grades', views.grades, name='grades'),
    path('conveniote/notes', views.notes_form, name='notes'),
    path('conveniote/syllabus', views.syllabus, name='syllabus'),
    path('conveniote/add_video_form_submssion/', views.add_video_form_submission, name = "addvideo"),
    path('conveniote/remove_video/', views.remove_video, name = "removevideo"),
    path('conveniote/assignment', views.assignment_form, name='assignment_form'),
    path('conveniote/evaluation', views.evaluation_form, name='evaluation_form'),
    path('conveniote/login', views.login_page, name='login'),
    path('conveniote/register', views.register, name='register'),
    path('conveniote/tos', views.tos, name='tos')

] 
