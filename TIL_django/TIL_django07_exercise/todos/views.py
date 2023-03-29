from django.shortcuts import render

# Create your views here.

from .models import Todo

def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'index.html', context)

def detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo': todo,
    }
    return render(request, 'detail.html', context)

def new(request):
    return render(request, 'new.html')


def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    number = request.GET.get('number')
    date = request.GET.get('date')


    todo = Todo(title=title, content=content, priority=number, deadline=date)
    todo.save()

    return render(request, 'create.html')