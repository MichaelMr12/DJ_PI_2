# для хранения представлений текущего приложения
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.template.defaultfilters import slugify, upper

menu = ['О сайте', 'Войти ', 'Обратная связь']


def index(request):
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    data = {'title': 'SFDSDF SDFSDF SDFSDF',
            'menu': menu,
            'float': 23.123,
            'value': 1,
            'url': upper("Очень крутой курсовик"),
            'url1': slugify("Очень крутой курсовик"),
            '12': 12,
            }
    # return render(request, 'women/index.html', context=data)
    # return render(request, 'women/index.html', {'title': 'Главная страница'})
    print(data)
    print('sdf')
    return render(request, 'women/index.html', data)


def categories(request, cat_id):
    return HttpResponse(f"<h1> статья под номером {cat_id} </h1>")


def categories_slug(request, cat):
    return HttpResponse(f"<h1> статья под категорией {cat} </h1>")


def categ(request):
    return HttpResponse("<h1> Страница с номером категорий </h1>")


def year_archive(request, year):
    if (int(year)) > 2023:
        raise Http404()
    if (int(year)) < 2000:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1> Год издания {year}</h1>")


def pageNotFound(request, exception):
    print(exception)
    return HttpResponseNotFound(f"<h1> Страница не найдена 11 <br>  {exception}</h1>")
