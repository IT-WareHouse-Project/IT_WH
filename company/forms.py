from django import forms
from django.core.exceptions import ValidationError
from .models import Company

# In case of errors in data:
#  raise ValidationError(_('Error Message'))

# Відомості про компанію:
class CompanyForm(forms.Form):
    # Обов'язкові поля:
    company_logo = forms.FileField(label='Лого компанії', help_text='Оберіть файл з логотипом компанії',
                                   allow_empty_file=False, required=False)
    company_title = forms.CharField(label='Назва компанії', max_length=200, required=True,
                                    initial='', help_text='Введіть назву компанії')
    company_code = forms.CharField(label='Код ЄДРПОУ', max_length=8, required=True,
                                   help_text='Код ЄДРПОУ складається із 8 цифр')

    # Не обов'язкові поля:
    city = forms.ChoiceField(label='Місто', required=False)
    address = forms.CharField(label='Адреса', max_length=250, required=False)

    email = forms.EmailField(label='Електрона пошта', required=False)
    phone = forms.CharField(label='Телефон', max_length=20, required=False)

    company_boss = forms.ChoiceField(label='Директор компанії', required=False)
    product_owner = forms.ChoiceField(label='МВ Особа', required=False,
                                      help_text='Оберіть Матеріально Відповідальну особу')

    comments = forms.CharField(label='Коментарі', max_length=500, widget=forms.Textarea, required=False, initial='')
