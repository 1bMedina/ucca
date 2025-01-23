from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import authenticate, login
#

def index(request):
    return render(request, 'ucca_web/index.html')

def about(request):
    return render(request, 'ucca_web/about.html')

def form(request):
    return render(request, 'ucca_web/form.html')
