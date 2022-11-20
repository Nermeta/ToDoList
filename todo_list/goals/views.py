from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Goal, Sub_Goal

# Create your views here.


class GoalList(LoginRequiredMixin, ListView):
    model = Goal
    context_object_name = 'goals'
    fields = ['complete']

   
class GoalCreate(CreateView):
    model = Goal
    fields = '__all__'

