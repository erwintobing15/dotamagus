from django.shortcuts import render
from .hero import names, ids

def index(request):
    names.sort()
    # modified the hereos name become image src
    # heroes_name = ['images/'+x+'.png' for x in names]
    return render(request, 'index.html', {'heroes_name': names})

def simulation(request):
    return render(request, 'simulation.html', {})
