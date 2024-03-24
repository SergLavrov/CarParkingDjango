from django.contrib import admin
from .models import Car, CarType, CarBrand
from django.contrib.auth.models import Permission

# Register your models here. Регистрация модели в админке !!!

admin.site.register(Car)
admin.site.register(CarType)
admin.site.register(CarBrand)
admin.site.register(Permission)   # Регистрация разрешения в админке
                                  # Т.е. мы можем создавать НОВЫЕ (СВОИ) разрешения в админке!