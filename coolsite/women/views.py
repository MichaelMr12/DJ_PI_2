# для хранения представлений текущего приложения
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Страница приложения women")


def categories(request, cat_id):
    return HttpResponse(f"<h1> статья под номером {cat_id} </h1>")

def categories_slug(request, cat):
    return HttpResponse(f"<h1> статья под категорией {cat} </h1>")

def categ(request):
    return HttpResponse("<h1> Страница с номером категорий </h1>")
