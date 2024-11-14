from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
def func1(request):
    title = 'Главная страница'
    return render(request, 'platform.html', )
def func2(request):
    title = 'Игры'
    l1 = "Atomic Heart"
    l2 = "Cyberpunk 2077"
    l3 = "PayDay2"
    l4 = "Купить"
    but = "Вернуться обратно"
    context = {
        'title': title,
        'l1': l1,
        'l2': l2,
        'l3': l3,
        'l4': l4,
        'but': but,
    }
    return render(request, 'games.html', context)
def func3(request):
    title = 'Извините, у вас 0 на счету'
    context = {
        'title': title,
    }
    return render(request, 'cart.html', context)