from django.shortcuts import render, redirect
from .models import Tarea
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_task(request):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        if descripcion:
            Tarea.objects.create(descripcion=descripcion)
            return redirect('/create/')  
    tareas = Tarea.objects.all().order_by("creada_en")
    return render(request, 'tasks/create_task.html',{"tareas": tareas})