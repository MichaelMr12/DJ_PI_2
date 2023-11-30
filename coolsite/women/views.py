# для хранения представлений текущего приложения
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.template.defaultfilters import slugify, upper

from women.models import Students

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Домашняя', 'url_name': 'home'},
        {'title': 'Категории', 'url_name': 'cats'},
        {'title': 'Красивый css', 'url_name': 'cub'},
        {'title': 'Список студентов', 'url_name': 'students'},
        ]

data_db = [{'id': 1, 'FIO': 'Снытко Руслан Николаевич', 'intresting': 'вязание, дизайн, верстка, вышивание крестиком',
            'diplom_red': True},
           {'id': 2, 'FIO': 'Король Богдан Александрович',
            'intresting': 'парашутный спорт, бокс , страйкбол,спортивный туризм', 'diplom_red': True},
           {'id': 3, 'FIO': 'Тузов Александр Максимович', 'intresting': 'курение, автомобили, спорт, компьютерные игры',
            'diplom_red': False},

           ]


def index(request):
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    data = {'title': 'Главная',
            'float': 23.123,
            'value': 1,
            'url': upper("Очень крутой курсовик"),
            'url1': slugify("Очень крутой курсовик"),
            '12': 12,
            'posts': data_db,
            'menu': menu,

            }
    # return render(request, 'women/index.html', context=data)
    # return render(request, 'women/index.html', {'title': 'Главная страница'})
    print(data)
    print('sdf')
    return render(request, 'women/index.html', data)


def students(request):
    posts = Students.objects.all()
    data = {'title': 'Список студентов',
            'menu': menu,
            'posts': posts,
            }
    return render(request, 'women/students.html', data)


def student(request, student_slug):
    post = get_object_or_404(Students, slug=student_slug)
    data = {'title': 'Профиль студента',
            'menu': menu,
            'post': post,
            }
    return render(request, 'women/student.html', data)


def about(request):
    return render(request, 'women/about.html', context={'menu': menu, 'title': 'О программе'})


def cub(request):
    return render(request, 'women/3D_kub.html', context={'menu': menu, 'title': 'Красивый css'})


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
