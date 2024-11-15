from django.shortcuts import render
from django.http import HttpResponse
from task5.forms import UserRegister

# Create your views here.
def sign_up_by_html(request):
    users = ["Linda", "Sarah", "kolin"]
    info = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if 18 <= int(age) <= 120 and password==repeat_password and username not in users:
            info = {
                'username': username,
                'password': password,
                'repeat_password': repeat_password,
                'age':age
            }
            return HttpResponse(f"Приветствуем, {username}!")
        else:
            if password != repeat_password:
                return HttpResponse(f"Пароли не совпадают")
            elif int(age)<18:
                return HttpResponse(f"Вы должны быть старше 18")
            elif username in users:
                return HttpResponse(f"Пользователь уже существует")
            info = {
                'error': [username, password, repeat_password,age]
            }
    return render(request, 'registration_page.html', context = info)

# def sign_up_by_django(request):
#     users = ["Linda", "Sarah", "kolin"]
#     if request.method == "POST":
#         info = UserRegister(request.POST)
#         if info.is_valid():
#             username = info.cleaned_data['username']
#             password = info.cleaned_data['password']
#             repeat_password = info.cleaned_data['repeat_password']
#             age = info.cleaned_data['age']
#             if age >= 18 and password == repeat_password and username not in users:
#                 HttpResponse(f"Приветствуем, {username}!")
#             else:
#                 info.key = 'error'
#                 if password != repeat_password:
#                     HttpResponse(f"Пароли не совпадают")
#                 elif age < 18:
#                     HttpResponse(f"Вы должны быть старше 18")
#                 elif username in users:
#                     HttpResponse(f"Пользователь уже существует")
#     else:
#         info = UserRegister()
#     print(f"Username: {username}")
#     print(f"Password: {password}")
#     print(f"Repeat_password: {repeat_password}")
#     print(f"Age: {age}")
#     return render(request, 'registration_page.html', {'form': info})
