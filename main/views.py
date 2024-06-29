from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context: dict = {
        'title': 'Home - Главная',
        'content': "Blumber's goods"
    }
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('About page')

def about(request):
    context: dict = {
        'title': 'О нас',
        'content': "Blumber's goods",
        'pagetext': "Наша интернет-магазин предлагает широчайший выбор строительных и сантехнических товаров.",
        'pagetext1':"Также планируется предоставление услуг по установке сантехнического оборудования и монтаж систем.",
        'pagetext2':"Связаться с нами: Телефон +78005553535"

    }
    return render(request, 'main/about.html', context)

