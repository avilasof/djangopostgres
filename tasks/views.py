from django.shortcuts import redirect, render
from .models import Task

# Create your views here.
def list_tasks(request):
    return render(request, 'list_tasks.html')

def create_task(request):
    task = Task(title=request.POST['title'], description=request.POST['description'])
    task.save()
    return redirect('/tasks/')
