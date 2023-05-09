from django.db import models
from employees.models import Employees


# Create your models here.
class DeviceType(models.Model):
    dev_type = models.CharField(max_length=150, unique=True, verbose_name='Тип пристрою')
    dev_type_logo = models.FileField(upload_to='dev_types/', default='dev_type.jpg', verbose_name='Лого категорії')

    def __str__(self) -> str:
        return str(self.dev_type).title()


class DeviceStatus(models.Model):
    dev_status = models.CharField(max_length=50, unique=True, verbose_name='Статус пристрою')

    def __str__(self) -> str:
        return str(self.dev_status).title()


class Vendors(models.Model):
    vendor = models.CharField(max_length=100, unique=True, verbose_name='Назва виробника')
    url = models.URLField(null=True, unique=True, verbose_name='Посилання на сайт')
    vendor_logo = models.FileField(upload_to='vendors/', default='dev_vendor.jpg', verbose_name='Лого виробника')

    def __str__(self) -> str:
        return str(self.vendor).title()


class Suppliers(models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name='Назва постачальника')
    url = models.URLField(null=True, unique=True, verbose_name='Посилання на сайт')
    email = models.EmailField(null=True, unique=True, verbose_name='Електрона пошта')
    phone = models.CharField(max_length=14, unique=True, verbose_name='Номер телефону')
    comments = models.TextField(max_length=500, null=True, verbose_name='Коментарі')

    def __str__(self) -> str:
        return str(self.title).title()


class DeviceWarranty(models.Model):
    warranty = models.CharField(max_length=100, unique=True, default='Без гарантії', verbose_name='Термін гарантії')

    def __str__(self) -> str:
        return str(self.warranty).lower()


class Devices(models.Model):
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE, verbose_name='Тип пристрою')
    device_vendor = models.ForeignKey(Vendors, on_delete=models.CASCADE, verbose_name='Виробник')
    device_title = models.CharField(max_length=250, verbose_name='Назва пристрою')
    device_model = models.CharField(max_length=100, null=True, verbose_name='Модель пристрою')
    serial_number = models.CharField(max_length=30, default='No Serial', verbose_name='Серійний номер')
    device_status = models.ForeignKey(DeviceStatus, null=True, on_delete=models.SET_NULL,
                                      verbose_name='Статус пристрою')
    user_id = models.ForeignKey(Employees, null=True, on_delete=models.SET_NULL, verbose_name='Користувач')
    supplier = models.ForeignKey(Suppliers, null=True, on_delete=models.SET_NULL, verbose_name='Постачальник')
    purchase_date = models.DateField(null=True, verbose_name='Дата придбання')
    device_warranty = models.ForeignKey(DeviceWarranty, null=True, on_delete=models.SET_NULL,
                                        verbose_name='Термін гарантії')
    comments = models.TextField(max_length=500, null=True, verbose_name='Коментарі')

    def __str__(self) -> str:
        return str(self.device_vendor).title() + ':' + str(self.device_title).title()
