from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from.models import Task


class TaskList(ListView):
    model= Task
    context_object_name= 'tasks'
    
    def get_context_data(self, **kwargs): 
       context= super().get_context_data(**kwargs)
       context['count']= context['tasks'].filter(complete=False).count()

       search_input=self.request.GET.get('search-area') or ''

       if search_input:
           context['tasks']= context['tasks'].filter(title__startswith=search_input)
           context['search_input']= search_input
       return context



class TaskDetail(DetailView):
    model= Task
    context_object_name= 'task'
    
class TaskCreate(CreateView): 
    model= Task
    fields= ['title','description', 'complete']
    success_url= reverse_lazy('tasks') 

class TaskUpdate( UpdateView):
    model= Task
    fields= ['title','description', 'complete']
    success_url= reverse_lazy('tasks')  


class TaskDelete( DeleteView):
    model =Task
    context_object_name='task'
    success_url= reverse_lazy('tasks')
