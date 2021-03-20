from django.http import HttpResponse
from django.shortcuts import render
from .models import Item

def home_page(request):
	return render(request, 'index.html')

def course1(request):
        return render(request, 'course1.html')

def video(request):
        obj=Item.objects.all()
        return render(request, 'video.html', {'obj':obj})

def grades(request):
        return render(request, 'grades.html')

def notes(request):
        return render(request, 'notes.html')

def syllabus(request):
        return render(request, 'syllabus.html')
