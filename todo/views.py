from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import DailyTodo
from .forms import TodoCreationForm
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('login')
    return render(request, 'login.html')

@login_required
def dashboard(request):
    from datetime import date
    user = request.user
    all_todos = DailyTodo.objects.filter(owner=request.user, DateStamp=date.today())
    print(all_todos)
    return render(request, 'dashboard.html', {'all_todos': all_todos, 'user': user})

def addTask(request):
    title = request.POST['title']
    task = DailyTodo(Title=title, owner=request.user)
    task.save()
    return redirect('dashboard')

def EditTodo(request, task_id):
    task = DailyTodo.objects.get(id=task_id)
    form = TodoCreationForm(instance=task)
    if request.method == 'POST':
        form = TodoCreationForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('dashboard')

    return render(request, 'editTodo.html', {'form': form, 'task':task})

def deleteTask(request, task_id):
    task = DailyTodo.objects.get(id=task_id)
    task.delete()
    return redirect('dashboard')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = auth.authenticate(username=username, password=raw_password)
            auth.login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})