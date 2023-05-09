from django.shortcuts import render

# Create your views here.
def page_403(request):
    return render(request, 'errors/page_403.html', context={
        'page_title': '403 Error Page',
        'app_name': 'Помилки',
        'page_name': '403'
    })


def page_404(request):
    return render(request, 'errors/page_404.html', context={
        'page_title': '404 Error Page',
        'app_name': 'Помилки',
        'page_name': '404'
    })


def login_error(request):
    return render(request, 'errors/login_error.html', context={
        'page_title': 'Помилка входу',
        'app_name': 'Помилки',
        'page_name': 'Помилка входу'
    })
