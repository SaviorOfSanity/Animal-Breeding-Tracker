from django.shortcuts import render
from django.http import HttpResponse
from .models import Animal

def index(request):
    animals = Animal.objects.filter()
    CATEGORY = [
        'Gecko',
        'Frog',
        'Fish',
        'Other',
    ]
    
    gecko = 0
    fish = 0
    frog = 0
    other = 0

    for animal in animals:
        if animal.animal_type == 'Gecko':
            gecko += 1
        elif animal.animal_type == 'Frog':
            frog += 1
        elif animal.animal_type == 'Fish':
            fish += 1
        else:
            other += 1
    stuff = [gecko, frog, fish, other]


    return render(request, 'animals/index.html', {
        'animals': animals,
        'labels': CATEGORY,
        'data': stuff, 
        })
