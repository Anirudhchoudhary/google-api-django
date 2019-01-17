from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from .models import Photo
from .forms import PhotoForm

# Create your views here.


class Home(TemplateView): 
    template_name = 'image/home.html'
    


def photo_list(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo')
    else:
        form = PhotoForm()
    return render(request, 'album/photo_list.html', {'form': form, 'photos': photos})    