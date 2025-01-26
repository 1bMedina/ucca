from django.shortcuts import render

from . import forms
from .models import Stoves


#

def index(request):
    return render(request, 'ucca_web/index.html')

def about(request):
    return render(request, 'ucca_web/about.html')

def form(request):
    all_stoves = Stoves.objects.all

    return render(request, 'ucca_web/form.html', {'all_stoves': all_stoves})

def search(request):
    stove_form = forms.StoveSearch()
    return render(request, 'ucca_web/form.html', {'stove_form': stove_form})