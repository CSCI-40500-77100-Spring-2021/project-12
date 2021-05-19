from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Item
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, AssignmentForm, NotesForm
from django.contrib.auth import authenticate, login, logout

def home_page(request):
	return render(request, 'index.html')

def front_page(request):
	return render(request, 'home.html')

def course1(request):
        return render(request, 'course1.html')

def video(request):
        obj=Item.objects.all()
        return render(request, 'video.html', {'obj':obj})

def grades(request):
        return render(request, 'grades.html')

def syllabus(request):
        return render(request, 'syllabus.html')

def tos(request):
        return render(request, 'tos.html')

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
        if request.method == 'POST':
                form = AssignmentForm(request.POST)
                if form.is_valid():
                        form = form.save()
        else:
                form = AssignmentForm()
        
        return render(request, 'assignment_form.html', {'form':form})

def notes_form(request):
        if request.method == 'POST':
                form = NotesForm(request.POST)
                if form.is_valid():
                        form = form.save()       
        return render(request, 'notes.html')

def evaluation_form(request):
        return render(request, 'evaluation_form.html')

def login_page(request):
        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('pass')

                user = authenticate(request, username = username, password = password)
                if user is not None:
                        login(request, user)
                        return redirect("home")
        return render(request, 'login.html')

def register(request):
        form = CreateUserForm()

        if request.method == 'POST':
                form = UserCreationForm(request.POST)
                print(form)
                if form.is_valid():
                        form.save()
                        return redirect("login")
        
        
        context = {'form': form}
        return render(request, 'register.html', context)
