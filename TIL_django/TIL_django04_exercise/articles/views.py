from django.shortcuts import render

# Create your views here.

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'catch.html', context)

def number_print(request, num):
    context = {
        'num': num,
    }
    return render(request, 'number_print.html', context)

def calculate(request, number1, number2):
    context = {
        'number1': number1,
        'number2': number2,
        'plus': number1 + number2,
        'minus': number1 - number2,
        'multiple': number1 * number2,
        'quot': number1 // number2,
    }
    return render(request, 'calculate.html', context)
