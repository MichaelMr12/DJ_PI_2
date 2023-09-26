from django.urls import path, register_converter

from women.classconvector import FourDigitYearConverter
from women.views import *

register_converter(FourDigitYearConverter, "yyyy")

urlpatterns = [

    path('', index, name='home'),
    path('categor/', categ, name='cats'),

    path('cats/<int:cat_id>/', categories, name='num_id'),
    path('cats/<slug:cat>/', categories_slug, name='cat_slug'),
    path("articles/<yyyy:year>/", year_archive, name='archive'),

]