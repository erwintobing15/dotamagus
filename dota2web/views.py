from django.shortcuts import render
from .hero import ids, names

def index(request):
    return render(request, 'index.html', {})

def simulation(request):
    names.sort()
    return render(request, 'simulation.html', {'names': names})
