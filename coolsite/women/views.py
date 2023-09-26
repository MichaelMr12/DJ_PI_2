# для хранения представлений текущего приложения
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    print(request.GET)
    return HttpResponse(f"Страница приложения women <br> ")


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
