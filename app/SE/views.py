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

def add_video_form_submission(request):
        obj=Item.objects.all()
        video_name = request.POST['url']
        video = Item(video = video_name)
        video.save()
        return render(request, 'video.html',{'obj':obj})

def remove_video(request):
        obj=list(Item.objects.all())
        video_name = request.POST['remove']
        idx = 0
        for video in obj:
                if(str(video) == str(video_name)):
                        break
                idx+=1
        list(Item.objects.all()).pop(idx)
        obj.pop(idx)
        Item.objects.all()[idx].delete()
        return render(request, 'video.html',{'obj':obj})

def assignment_form(request):
        return render(request, 'assignment_form.html')

def evaluation_form(request):
        return render(request, 'evaluation_form.html')
