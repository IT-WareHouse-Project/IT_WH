from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail

# Create your views here.
# index             - Головна сторінка сайту, яка зустрічає користувача.
# forgot_password   - Форма відновлення паролю
# logout            - Вихід користувача із системи


def index(request):
    # Якщо користувач не авторізован - робимо логін:
    if not request.user.is_authenticated:
        # GET Request:  Відображення сторінки
        if request.method == 'GET':
            return render(request, 'home/index.html', context={
                'page_title': 'Вхід до системи',
                'app_name': '',
                'page_name': 'Логін'
            })

        # POST Request: Обробка даних й логін
        elif request.method == 'POST':
            # 1. Отримуємо потрібні дані із запроса:
            user_login = request.POST.get('user_name')
            user_password = request.POST.get('user_pass')

            if request.POST.get('keep_logged') is None:
                user_keep = False
            else:
                user_keep = True

            # 2. Перевіряємо відповідність Логіну і Паролю:
            user = authenticate(request, username=user_login, password=user_password)

            # 3. Обробляємо результат перевірки:
            if user is None:
                # Логін або Пароль задані не вірно => Login Error
                return redirect("/errors/login_error")

            else:
                if not user.is_active:
                    # Акаунт користувача не активний (заблокований) => Login Error:
                    return redirect("/errors/login_error")

                # 4. Дані успішно перевірені:
                login(request, user)
                return redirect("/itwh/main_page")

        else:
            # UNKNOWN Request:  Error 404:
            return redirect("/errors/page_404")
    else:
        # Якщо користувач авторизован - переходимо на головну сторінку проекту:
        return redirect("/itwh/main_page")


# Відновлення паролю користувача:
# 1. Якщо користувач вже авторизований у системі - відновлювати пароль через цю форму не має сенсу
# 2. Ця форма працює лише у випадку, коли користувач не авторизований у системі
def forgot_password(request):
    if not request.user.is_authenticated:
        if request.method == 'GET':
            return redirect('/password-reset')

        else:
            return redirect("/errors/page_404")
    else:
        # Зробити переадресацію на сторінку "Мій профіль", де авторізований користувач має
        # змогу змінити свій пароль
        return redirect("/accounts/my_profile")


# Вихід із системи:
def user_logout(request):
    logout(request)
    return redirect("/")
