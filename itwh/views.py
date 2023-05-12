from django.shortcuts import render, redirect
from employees.models import *
from company.models import *
from assets.models import *

# Create your views here.
# Головна сторінка - DashBoard
def main_page(request):
    if not request.user.is_authenticated:
        # Якщо користувач не авторизований - перехід на сторінку авторизації
        return redirect("/")

    else:
        return render(request, 'itwh/main_page.html', context={
            'page_title': 'Головна сторінка',
            'app_name': 'IT WH',
            'page_name': 'Головна сторінка',
        })
