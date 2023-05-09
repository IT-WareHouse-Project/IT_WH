from django.shortcuts import render, redirect

# Create your views here.
# Головна сторінка - DashBoard
def main_page(request):
    if not request.user.is_authenticated:
        # Якщо користувач не авторизований - перехід на сторінку авторизації
        return redirect("/")

    else:
        # Якщо користувач авторизований - визначаємо його базові параметри:
        # user_id:
        # user_email:
        # user_firstname:
        # user_lastname:
        # user_group:
        # determine user's group:
        user_data = {}
        user_data['u_id'] = request.user.id
        user_data['u_email'] = request.user.email

        user_data['u_fname'] = request.user.first_name
        user_data['u_lname'] = request.user.last_name

        if request.user.groups.filter(name='Admins').exists():
            user_data['u_group'] = 'Admins'
        elif request.user.groups.filter(name='Users').exists():
            user_data['u_group'] = 'Users'
        else:
            user_data['u_group'] = 'None'

        print(user_data)

        return render(request, 'itwh/main_page.html', context={
            'page_title': 'Головна сторінка',
            'app_name': 'IT WH',
            'page_name': 'Головна сторінка',
            'user_data': user_data
        })
