from django.shortcuts import render, redirect
from .models import Album
from .forms import AlbumForm

# Create your views here.

def index(request):
    albums = Album.objects.all()
    context = {
        'albums': albums,
    }
    return render(request, 'albums/index.html', context)


def detail(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'album': album,
    }
    return render(request, 'albums/detail.html', context)


def create(request):
    
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save()
            return redirect('albums:detail', album.pk)
    else:
        form = AlbumForm()
    context = {
        'form': form,
    }
    return render(request, 'albums/new.html', context)


def update(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('albums:detail', album.pk)
    else:
        form = AlbumForm(instance=album)
    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'albums/update.html', context)

def delete(request, pk):
    album = Album.objects.get(pk=pk)
    album.delete()
    return redirect('albums:index')
