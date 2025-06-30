from django.shortcuts import render, redirect
from .models import Tarea, User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required
@csrf_exempt
def create_task(request):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        if descripcion:
            Tarea.objects.create(
                descripcion=descripcion,
                usuario=request.user  
            )
            return redirect('/create/')  
    tareas = Tarea.objects.all().order_by("creada_en")
    return render(request, 'tasks/create_task.html',{"tareas": tareas})

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            print(f" Usuario {username} autenticado correctamente")
            return redirect("create_task")
        else:
            return render(request, "tasks/login.html", {"error": "Invalid credentials"})
    
    return render(request, "tasks/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")
