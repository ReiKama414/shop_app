from django.shortcuts import render, redirect
from .forms import UploadModelForm
from .models import Photo

def index(request):
    photos = Photo.objects.all()
    form = UploadModelForm()

    context = {
        'photos': photos,
        'form': form
    }

    return render(request, 'index.html', context)

def adopt(request, pk):
    photos = Photo.objects.get(id=pk)

    if request.method == "POST":
        photos.delete()
        return redirect('/photos')

    context = {
        'photos': photos
    }

    return render(request, 'adopt.html', context)

def new_photo(request):
    photos = Photo.objects.all()
    form = UploadModelForm()

    if request.method == "POST":
        form = UploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/photos')

    context = {
        'photos': photos,
        'form': form
    }

    return render(request, 'new_photo.html', context)