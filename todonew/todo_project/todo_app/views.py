#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.order_by('-created_at')
    form = TaskForm()
    return render(request, 'todo_app/index.html', {'tasks': tasks, 'form': form})

@require_POST
def add_task(request):
    form = TaskForm(request.POST)

    if form.is_valid():
        new_task = form.save()
    
    return redirect('index')

def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()

    return redirect('index')

def complete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = not task.completed
    task.save()

    return redirect('index')
