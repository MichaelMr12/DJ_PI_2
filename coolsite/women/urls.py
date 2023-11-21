from django.urls import path, register_converter

from women.classconvector import FourDigitYearConverter
from women.views import *

register_converter(FourDigitYearConverter, "yyyy")

urlpatterns = [

    path('', index, name='home'),
    path('about/', about, name='about'),
    path('categor/', categ, name='cats'),
    path('cub/', cub, name='cub'),
    path('students/<slug:student>/', students, name='student_slug'),

    path('cats/<int:cat_id>/', categories, name='num_id'),
    path('cats/<slug:cat>/', categories_slug, name='cat_slug'),
    path("articles/<yyyy:year>/", year_archive, name='archive'),

]
