from django.shortcuts import render, redirect, get_object_or_404
from .models import Company
from .forms import CompanyForm

# Create your views here.
def index(request):
    # 1. Basic information:
    context = {
        'page_title': 'Компанія',
        'app_name': 'Копанія',
        'page_name': 'Компанія'
    }

    if len(Company.objects.all()) == 0:
        context['company_count'] = 0
    else:
        context['company_count'] = 1
        context['company_info'] = Company.objects.all()

    # Just for test:
    print(context)

    # Return the result page:
    return render(request, 'company/index.html', context=context)


def details(request):
    company_info = Company.objects.all()

    if len(company_info) == 0:
        print('There is no company, please add new company via URL.')
        company_number = 0
    else:
        company_number = len(company_info)

        for cmp in company_info:
            print(cmp.id)
            print(cmp)


    context = {
        'page_title': 'Інформація про компанію',
        'app_name': 'Компанія',
        'page_name': 'Деталі компанії',
        'company_info': cmp,
        'company_count': company_number
    }

    return render(request, 'company/details.html', context=context)


def create(request):
    # С Початку потрібно перевірити, чи є вже компанія в Базі даних:
    # якщо компанія вже існує то можно лише зробити апдейт
    company_info = Company.objects.all()

    if request.method == 'GET':
        if len(company_info) > 0:
            return redirect('/company/update')

        else:
            context = {
                'page_title': '',
                'app_name': '',
                'page_name': '',
                'form': CompanyForm
            }

            return render(request, 'company/create.html', context=context)

    elif request.method == 'POST':
        filled_form = CompanyForm(request.POST, request.FILES)

        if filled_form.is_valid():
            company_data = Company()

            company_data.company_logo = filled_form.cleaned_data['company_logo']
            company_data.company_title = filled_form.cleaned_data['company_title']
            company_data.company_code = filled_form.cleaned_data['company_code']

            company_data.save()

        return redirect('/itwh/main_page')

    else:
        return redirect('/errors/page_404')


def update(request):
    pass

def delete(request):
    company_info = Company.objects.all()
    company_id = company_info.id

    print(company_id)
    return redirect('/itwh/main_page')
