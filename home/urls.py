from django.urls import path
from .views import index, user_logout, forgot_password
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', index, name='user_login'),
    path('user_logout', user_logout, name='user_logout'),
    path('forgot_password', forgot_password),
    path('password-reset', auth_views.PasswordResetView.as_view(template_name='home/forgot_password.html'),
         name='password-reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='home/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='home/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='home/password_reset_complete.html'),
         name='password_reset_complete'),
]
