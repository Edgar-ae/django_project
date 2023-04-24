from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .models import Project, Task

from django.shortcuts import get_list_or_404

from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title = 'Django Course!!'
    return render(request, 'index.html', {
        'title': title
    })

def hello(request, username):
    #return render(request, 'signup.html')
    return HttpResponse("<h2>Hello %s</h2>" % username)

def about(request):
    return render(request, 'about.html')

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    # return JsonResponse(projects, safe=False)
    return render(request, 'projects/projects.html', {
        'projects': projects
    })

def tasks(request):
    tasks = Task.objects.all()
    # task = Task.objects.get(id=id)
    # return HttpResponse('tasks: %s' %task.title)
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html',{
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('n_create_task')
    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        print(request.POST)
        project = Project. objects.create(name=request.POST["name"])
        return redirect('n_projects')