from django.urls import path

from women.views import *

urlpatterns = [

    path('', index),
    path('categor/', categ),

    path('cats/<int:cat_id>/', categories),
    path('cats/<slug:cat>/', categories_slug),

]
