from django.urls import path
from .views import index, create, details, update, delete


urlpatterns = [
    path('', index),
    path('create', create),
    path('details', details),
    path('update', update),
    path('delete', delete)
]