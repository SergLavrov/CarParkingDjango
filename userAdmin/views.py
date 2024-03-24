from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.


# РЕГИСТРАЦИЯ НОВОГО ПОЛЬЗОВАТЕЛЯ

# Подробное разъяснение по строкам:
#
# def signup(request: HttpRequest): - Это объявление функции signup, которая принимает объект запроса request
# типа HttpRequest. Это означает, что функция предназначена для обработки HTTP-запросов.
#
# if request.method == 'POST': - Здесь происходит проверка, является ли метод запроса POST.
# Метод запроса - это HTTP-метод, используемый для отправки запроса (например, GET, POST, PUT, DELETE).
#
# username = request.POST['username'] - Здесь извлекается значение поля username из POST-запроса.
# В Django, объект запроса имеет словарь POST, содержащий данные, отправленные методом POST.
# email = request.POST['email'] - Аналогично, извлекается значение поля email из POST-запроса.
# password = request.POST['password'] - Здесь извлекается значение поля password из POST-запроса.
#
# group_user = Group.objects.get(name='user') - Здесь происходит извлечение объекта группы с именем 'user'
# из базы данных. В Django, Group - это модель, представляющая группу пользователей.

# user = User.objects.create_user(username, email, password) - Эта строка создает нового пользователя
# в системе, используя предоставленное имя пользователя, электронную почту и пароль.
# User - это модель, представляющая пользователя в Django.
#
# user.groups.add(group_user) - Здесь новый пользователь добавляется в группу 'user',
# что может использоваться для управления разрешениями и привилегиями пользователя.
#
# user.save() - Эта строка сохраняет информацию о новом пользователе в базе данных.
#
# return HttpResponseRedirect(reverse('login_user')) - В случае успешной регистрации переходим
# на страницу АУТЕНТИФИКАЦИИ ПОЛЬЗОВАТЕЛЯ !!!

# else: - Если метод запроса НЕ является POST, то выполняется следующий блок кода.
# return render(request, 'userAdmin/signup.html') - Здесь отображается шаблон 'signup.html'
# с использованием данных из запроса. В Django функция render используется для отображения HTML-шаблонов.

def signup(request: HttpRequest):               # РЕГИСТРАЦИЯ НОВОГО ПОЛЬЗОВАТЕЛЯ
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        group_user = Group.objects.get(name='user')

        user = User.objects.create_user(username, email, password)
        user.groups.add(group_user)
        user.save()

        return HttpResponseRedirect(reverse('login_user'))
    else:
        return render(request, 'userAdmin/signup.html')


# АУТЕНТИФИКАЦИЯ ПОЛЬЗОВАТЕЛЯ

# Определяется функция с именем login_user, принимающая объект HttpRequest
# в качестве аргумента.
#
# Проверяется, является ли метод запроса 'POST'.
#
# Извлекаются значения имени пользователя и пароля из объекта запроса.
#     username = request.POST['userName']
#     password = request.POST['password']
#
# Происходит попытка аутентификации пользователя с использованием
# полученного имени пользователя и пароля.
# user = authenticate(request, username=username, password=password)
#
# Проверяется, успешна ли аутентификация.
# if user is not None:
#
# Если аутентификация прошла успешно, пользователь выполняет вход
# и перенаправляется на страницу для просмотра автомобилей.
# login(request, user)
# return HttpResponseRedirect(reverse('get-cars'))
#
# Если аутентификация НЕ удалась, отображается страница входа.
# return render(request, 'userAdmin/login.html')

# else: - Если метод запроса НЕ является POST, то выполняется следующий блок кода.
# return render(request, 'userAdmin/login.html') - Здесь отображается шаблон для АУТЕНТИФИКАЦИИ ПОЛЬЗОВАТЕЛЯ!
# В Django функция render используется для отображения HTML-шаблонов.


def login_user(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST['userName']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:                                    # None - если пользователь НЕ найден или НЕВЕРНО введен пароль !!!
            login(request, user)                                # is not None - если пользователь найден и верно введен пароль !!!
            return HttpResponseRedirect(reverse('get-cars'))

        return render(request, 'userAdmin/login.html')

    else:
        return render(request, 'userAdmin/login.html')


# БЫЛ 1 ВАРИАНТ
# def login_user(request: HttpRequest):
#     if request.method == 'POST':
#         return HttpResponse('Login')
#     else:
#         return render(request, 'userAdmin/login.html')


def logout_user(request: HttpRequest):
    logout(request)
    return HttpResponseRedirect(reverse('get-cars'))

# def logout_user(request: HttpRequest):
#     # Определяет функцию с именем `logout_user`, которая принимает
#     объект `HttpRequest` в качестве аргумента
#
#     logout(request)
#     # Вызывает функцию `logout` с объектом `request`
#
#     return HttpResponseRedirect(reverse('login_user'))
#     # Возвращает ответ-редирект на URL 'login_user'