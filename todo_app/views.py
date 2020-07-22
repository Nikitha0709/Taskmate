from django.shortcuts import render,redirect
from django.http import HttpResponse
from todo_app.models import TaskList
from todo_app.form import Taskform
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# from todo_app import template
# Create your views here.
@login_required
def home(request):
    if request.method == "POST":
        
        forms=Taskform(request.POST or None)
        
        if forms.is_valid():
            instance=forms.save(commit=False)
            instance.manage=request.user
            instance.save()
            messages.success(request,("NEW TASK ADDED"))
        return redirect('/task')

    else:
        all_tasks=TaskList.objects.filter(manage=request.user)
        paginator=Paginator(all_tasks,5)
        page=request.GET.get('pg')
        all_tasks=paginator.get_page(page)
        return render(request,'home.html',{'all_tasks': all_tasks})
def delete_task(request,task_id):
    
    task=TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
    else:
        messages.error(request,("You can't acess to this page!!"))
    return redirect('/task')
def edit_task(request,task_id):
    if request.method == "POST":
        task=TaskList.objects.get(pk=task_id)
        forms=Taskform(request.POST or None,instance=task)
        if forms.is_valid():
            forms.save()
            messages.success(request,("TASK IS EDITED"))
        return redirect('task')

    else:
        task_obj=TaskList.objects.get(pk=task_id)
        return render(request,'edit.html',{'task_obj': task_obj})
def done_task(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done=True
        task.save()
    else:
         messages.error(request,("You can't acess to this page!!"))
    return redirect('/task')
def pending_task(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done=False
        task.save()
    else:
        messages.error(request,("You can't acess to this page!!"))
    return redirect('/task')
def contactus(request):
     return render(request,'Contact.html',{})
def about(request):
    return render(request,'About.html',{})
def index(request):
    return render(request,'index.html',{})
