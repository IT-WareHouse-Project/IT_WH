from django.db import models


# Create your models here.
# Таблиця Відділів (Департаментів) компанії:
class Departments(models.Model):
    department = models.CharField(max_length=150, unique=True, verbose_name='Назва відділу')

    # Презентація (Відображення):
    def __str__(self) -> str:
        return str(self.department).title()


# Таблиця Назви міст:
class Cities(models.Model):
    city = models.CharField(max_length=100, unique=True, verbose_name='Назва міста')

    def __str__(self) -> str:
        return str(self.city).title()


# Таблиця Розміщення (Локацій)
class Locations(models.Model):
    city = models.ForeignKey(Cities, null=True, on_delete=models.SET_NULL, verbose_name='Назва міста')
    location = models.CharField(max_length=100, default='null', verbose_name='Локація')
    comments = models.TextField(max_length=500, default='null', verbose_name='Коментарі')

    def __str__(self) -> str:
        return str(self.city).title() + ':' + str(self.location)


# Головна таблиця Співробітників
class Employees(models.Model):
    photo = models.FileField(upload_to='photos/', default='default_user.jpg', verbose_name='Фото співробітника')
    firstname = models.CharField(max_length=100, verbose_name='Ім"я')
    lastname = models.CharField(max_length=100, verbose_name='Прізвище')
    eid = models.CharField(max_length=10, unique=True, verbose_name='Внутрішній номер')
    email = models.EmailField(unique=True, verbose_name='Електрона пошта')
    department = models.ForeignKey(Departments, null=True, on_delete=models.SET_NULL, verbose_name='Назва відділу')
    title = models.CharField(max_length=150, verbose_name='Посада')
    mobilephone = models.CharField(max_length=14, unique=True, verbose_name='Мобільний телефон')
    location = models.ForeignKey(Locations, null=True, on_delete=models.SET_NULL, verbose_name='Локація')

    def __str__(self) -> str:
        return str(self.firstname).title() + str(self.lastname).title()
