from http.client import HTTPResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
def omlet_view(request, servings= 'none'):
    servings = int(request.GET.get("servings", 1))
    omlet = {}
    for k, v in DATA['omlet'].items():
        omlet[k] = v * servings

    context = {
    'recipe' : omlet
    }
    return render(request, 'calculator/index.html', context)

def pasta_view(request, servings= 'none'):
    servings = int(request.GET.get("servings", 1))
    pasta = {}
    for k, v in DATA['pasta'].items():
        pasta[k] = v * servings

    context = {
    'recipe' : pasta
    }
    return render(request, 'calculator/index.html', context)

def buter_view(request, servings= 'none'):
    servings = int(request.GET.get("servings", 1))
    buter = {}
    for k, v in DATA['buter'].items():
        buter[k] = v * servings

    context = {
    'recipe' : buter
    }
    return render(request, 'calculator/index.html', context)
