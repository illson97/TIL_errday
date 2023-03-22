from django.shortcuts import render

# Create your views here.

import random
def today_dinner(request):
    foods = ['치킨','삼겹살','짜장면','짬뽕',]
    picked = random.choice(foods)
    context = {
        'foods': foods,
        'picked': picked,
    }
    return render(request, 'today_dinner.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'catch.html', context)


def lotto_create(request):
    return render(request, 'lotto_create.html')

def lotto(request):
    message = request.GET.get('number')
    context = {
        'number': number,
    }
    return render(request, 'lotto.html', context)