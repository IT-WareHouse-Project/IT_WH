from django.db import models
from employees.models import Cities, Employees


# Create your models here.
class Company(models.Model):
    # Обов'язкові поля:
    company_logo = models.FileField(upload_to='company/', default='def-logo.jpg', verbose_name='Логотип компанії')
    company_title = models.CharField(max_length=200, unique=True, default='', verbose_name='Назва компанії')
    company_code = models.CharField(max_length=8, unique=True, default='', verbose_name='Код ЄДРПОУ')

    # НЕ обов'язкові поля:
    # Адреса компанії:
    city = models.ForeignKey(Cities, null=True, on_delete=models.SET_NULL, verbose_name='Місто')
    address = models.CharField(max_length=250, null=True, verbose_name='Адреса')

    # Контакти компанії:
    email = models.EmailField(null=True, verbose_name='Електрона пошта')
    phone = models.CharField(max_length=20, null=True, verbose_name='Номер телефона')

    # Директор, Матеріально відповідальна особи:
    company_boss = models.ForeignKey(Employees, related_name='company_boss', null=True,
                                     on_delete=models.SET_NULL, verbose_name='Директор')
    product_owner = models.ForeignKey(Employees, related_name='product_owner', null=True,
                                      on_delete=models.SET_NULL, verbose_name='МВ Особа')

    # Будь які, додаткові коментарі:
    comments = models.TextField(max_length=500, null=True, default='', verbose_name='Додаткові коментарі:')


    def __str__(self) -> str:
        return str(self.company_title).title() + ' (ЄДРПОУ: ' + str(self.company_code) + ')'
