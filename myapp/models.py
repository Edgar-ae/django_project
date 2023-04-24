from django.db import models

# Create your models here.

class Project(models.Model):#Creamos una tabla llamda Project
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Task(models.Model): #Creamos una tabla llamada Task
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE) #El CASCADE es para que el Task se elimine en cascada sise eliminar el Project
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title+" - "+self.project.name