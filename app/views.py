from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('show_time'),
        'Показать содержимое рабочей директории': reverse('show_workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    listdir = os.listdir()
    listdir_output = ['<ol>']
    for name in listdir:
        listdir_output.append(f'<li> {name}</li>')
    listdir_output.append('</ol>')

    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    return HttpResponse(listdir_output)
