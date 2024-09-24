from django.shortcuts import render
from .models import Task
# Create your views here.

def get_all_tasks(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request,'task/tasks.html',context=context)