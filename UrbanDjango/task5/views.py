from django.shortcuts import render
from django.http import HttpResponse
from task5.forms import UserRegister

# Create your views here.
def control(username, password, repeat_password, age, users):
    info = {}
    if username in users:
        info = "Пользователь уже существует"
        return  info
    elif password != repeat_password:
        info = "Пароли не совпадают"
        return  info
    elif int(age) < 18:
        info = "Вы должны быть старше 18"
        return  info

    info =  f'Приветствуем {username}'
    return info

# def sign_up_by_html(request):
#     users = ["Linda", "Sarah", "kolin"]
#     info = {}
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         repeat_password = request.POST.get('repeat_password')
#         age = request.POST.get('age')
#         str = control(username, password, repeat_password, age, users)
#         info = {"error": str}
#         return render(request, 'registration_page.html', info)
#     info = {}
#     return render(request, 'registration_page.html', info)
def sign_up_by_django(request):
    users = ["Linda", "Sarah", "kolin"]
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            str = control(username, password, repeat_password, age, users)
            info = {"error": str}
            return render(request, 'registration_page.html', info)
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form})
