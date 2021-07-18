from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TodoList, Category
import datetime

# Create your views here.

def home(request):
    return render(request, 'bear.html')

def AboutMe(request):
    return render(request, 'aboutme.html')

def Resume(request):
    return render(request, 'resume.html')

def index(request):
    todos = TodoList.objects.all()
    categories = Category.objects.all()
    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST["description"]
            date = str(request.POST["date"])
            category = request.POST["category_select"]
            content = title + " -- " + date + " " + category
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save()
            return redirect(request, 'todo.html')

        if "taskDelete" in request.POST:
            checkedlist = request.POST["checkedbox"]
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id))
                todo.delete()

        if "taskComplete" in request.POST:
            checkedlist = request.POST["checkedbox"]
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id)) 
                
    return render(request, 'todo.html', {"todos": todos, "categories": categories})