from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def simulation(request):
    return render(request, 'simulation.html', {})
