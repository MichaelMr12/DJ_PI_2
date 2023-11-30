from django.urls import path, register_converter

from women.classconvector import FourDigitYearConverter
from women.views import *

register_converter(FourDigitYearConverter, "yyyy")

urlpatterns = [

    path('', index, name='home'),
    path('about/', about, name='about'),
    path('categor/', categ, name='cats'),
    path('cub/', cub, name='cub'),
    path('students/', students, name='students'),
    path('students/<slug:student_slug>/', student, name='student'),

    path('cats/<int:cat_id>/', categories, name='num_id'),
    path('cats/<slug:cat>/', categories_slug, name='cat_slug'),
    path("articles/<yyyy:year>/", year_archive, name='archive'),

]
