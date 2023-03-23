from django.shortcuts import render

# Create your views here.

def detail(request, num):
    context = {
        'num': num,
    }
    return render(request, 'detail.html', context)

def greeting(request, name):
    context = {
        'name': name,
    }
    return render(request, 'greeting.html', context)