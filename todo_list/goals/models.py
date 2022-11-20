from django.db import models
from django.contrib.auth.models import User
from tasks.models import Task

# Create your models here.

class Goal(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank =False)
    title = models.CharField(max_length=200)
    description =  models.TextField()
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    tasks = models.ManyToManyField(Task)

class Sub_Goal(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank =False)
    parent_goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description =  models.TextField()
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    tasks = models.ManyToManyField(Task)

class PreReq (models.Model):
    goal = models.ManyToManyField(Goal)
    PreReq = models.ManyToManyField(Sub_Goal)