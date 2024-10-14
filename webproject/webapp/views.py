from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import ToDolist

# Create your views here.

def home(request):
    data=ToDolist.objects.all()
    obj={"data":data}
    return render(request,"home.html",obj)

def save_data(request):
    print(request.POST)
    ToDolist.objects.create(
        new_task=request.POST['new_task'],
        new_date=request.POST['new_date'],
    )
    return redirect("/")

def delete_todo(request):
    id=request.GET['id']
    ToDolist.objects.filter(id=id).delete()
    return redirect("/")

def edit_todolist(request):
    info=ToDolist.objects.get(id=request.GET['id'])
    obj={"info":info}
    return render(request,"edit_todolist.html",obj)

def update_todolist(request):
    print(request.POST)
    todo=ToDolist.objects.get(id=request.POST['id'])
    todo.new_task=request.POST['new_task']
    todo.new_date=request.POST['new_date']
    todo.save()
    return redirect('/')
