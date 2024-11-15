from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
def func1(request):
    title = 'Главная страница'
    context = {
        'title': title,
    }
    return render(request, 'platform.html', context)
def func2(request):
    title = 'Игры'
    games = ["Atomic Heart", "Cyberpunk 2077",  "PayDay2"]
    l4 = "Купить"
    context = {
        'title': title,
        'games': games,
        'l4': l4,
    }
    return render(request, 'games.html', context)
def func3(request):
    title = 'Извините, у вас 0 на счету'
    context = {
        'title': title,
    }
    return render(request, 'cart.html', context)