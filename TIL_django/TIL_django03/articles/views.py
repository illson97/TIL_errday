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