from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="n_index"),
    path('hello/<str:username>', views.hello, name="n_hello"),
    path('about', views.about, name="n_about"),
    path('projects', views.projects, name="n_projects"),
    path('tasks', views.tasks, name="n_tasks"),
    path('create_task', views.create_task, name="n_create_task"),
    path('create_project', views.create_project, name="n_create_project")

]