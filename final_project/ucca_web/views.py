from django.shortcuts import render

from . import forms
from .models import Stoves


#

def index(request):
    return render(request, 'ucca_web/index_2.html')

def builder(request):
    return render(request, 'ucca_web/builders.html')

def support(request):
    return render(request, 'ucca_web/support.html')

def about(request):
    return render(request, 'ucca_web/about.html')

def form(request):
    all_stoves = Stoves.objects.all()

    return render(request, 'ucca_web/form.html', {'all_stoves': all_stoves})

def search(request):
    if request.method == 'POST':
        stove_form = forms.StoveSearch(request.POST)
        if stove_form.is_valid():
            form.save()
    else:
        stove_form = forms.StoveSearch()
    return render(request, 'ucca_web/form.html', {'stove_form': stove_form})