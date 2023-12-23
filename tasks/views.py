from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Task
from .forms import *

def indexView(request):
    
    tasks = Task.objects.all()
    form = TaskForm()

    context = {
        "tasks": tasks,
        "form": form,
    }

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        
    return render(request, "tasks/index.html", context)

def editView(request, pk):

    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    context = {
        "form": form,
    }

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("index")

    return render(request, "tasks/edit.html", context)

def deleteView(request, pk):
    task = Task.objects.get(id=pk)
    context = {
        "task": task,
    }

    if request.method == "POST":
        task.delete()
        return redirect("index")
    
    return render(request, "tasks/delete.html", context)