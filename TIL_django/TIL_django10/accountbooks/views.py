from django.shortcuts import render, redirect
from .models import AccountBook
from .forms import AccountBookForm

# Create your views here.

def index(request):
    accountbooks = AccountBook.objects.all()
    context = {
        'accountbooks': accountbooks,
    }
    return render(request, 'accountbooks/index.html', context)

def detail(request, pk):
    accountbook = AccountBook.objects.get(pk=pk)
    context = {
        'accountbook': accountbook,
    }
    return render(request, 'accountbooks/detail.html', context)


                  
def create(request):
    
    if request.method == 'POST':
        form = AccountBookForm(request.POST)
        if form.is_valid():
            accountbook = form.save()
            return redirect('accountbooks:detail', accountbook.pk)
    else:
        form = AccountBookForm()
    context = {
        'form': form,
    }
    return render(request, 'accountbooks/new.html', context)



def update(request, pk):
    accountbook = AccountBook.objects.get(pk=pk)
    if request.method == 'POST':
        form = AccountBookForm(request.POST, instance=accountbook)
        if form.is_valid():
            form.save()
            return redirect('accountbooks:detail', accountbook.pk)
    else:
        form = AccountBookForm(instance=accountbook)
    context = {
        'accountbook': accountbook,
        'form': form,
    }
    return render(request, 'accountbooks/update.html', context)

def delete(request, pk):
    accountbook = AccountBook.objects.get(pk=pk)
    accountbook.delete()
    return redirect('accountbooks:index')