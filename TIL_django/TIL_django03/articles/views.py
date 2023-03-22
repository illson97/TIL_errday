from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


import random
def dinner(request):
    foods = ['족발','햄버거','치킨','초밥',]
    picked = random.choice(foods)
    context = {
        'foods': foods,
        'picked': picked,
    }
    return render(request, 'dinner.html', context)

def search(request):
    return render(request, 'search.html')

def fakeNaver(request):
    return render(request, 'fakeNaver.html')

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'catch.html', context)