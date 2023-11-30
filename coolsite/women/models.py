# для хранения ORM- моделей и для представления данных из базы данных
from django.db import models

# Create your models here.
from django.urls import reverse

data_db = [{'id': 1, 'FIO': 'Снытко Руслан Николаевич', 'intresting': 'вязание, дизайн, верстка, вышивание крестиком',
            'diplom_red': True},
           {'id': 2, 'FIO': 'Король Богдан Александрович',
            'intresting': 'парашутный спорт, бокс , страйкбол,спортивный туризм', 'diplom_red': True},
           {'id': 3, 'FIO': 'Тузов Александр Максимович', 'intresting': 'курение, автомобили, спорт, компьютерные игры',
            'diplom_red': False},

           ]


# https://docs.djangoproject.com/en/4.2/ref/models/fields/
class Students(models.Model):
    fio = models.CharField(max_length=50)
    interesting = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    diplom_red = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('student', kwargs={'student_slug': self.slug})
