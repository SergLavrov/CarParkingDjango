from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from .models import CarType, CarBrand, Car, ParkingSlot, Parking

# Create your views here.

def initialize(request):                  # Функция initialize - просто для первичного заполнения БД !!!
    try:
        car_types = [
            CarType(name='Sedan'),
            CarType(name='Hatchback'),
            CarType(name='Minivan'),
            CarType(name='Coupe'),
            CarType(name='Crossover'),
            CarType(name='SUV'),
            CarType(name='Pickup'),
        ]

        car_brands = [
            CarBrand(name='Audi'),
            CarBrand(name='BMW'),
            CarBrand(name='Chevrolet'),
            CarBrand(name='Mercedes'),
            CarBrand(name='Mazda'),
            CarBrand(name='Mitsubishi'),
            CarBrand(name='Ford'),
            CarBrand(name='KIA'),
            CarBrand(name='Hyundai'),
            CarBrand(name='Citroen'),
            CarBrand(name='Renault'),
            CarBrand(name='Nissan'),
        ]

        parks = [
            Parking(name='Parking 1', address='ул.Суворова, 25', phone_number='Phone 1', price=1.0),
            Parking(name='Parking 2', address='ул. Димитрова, 30', phone_number='Phone 2', price=2.0),
        ]

        park_slots_1 = [
            ParkingSlot(number=1),
            ParkingSlot(number=2),
            ParkingSlot(number=3),
            ParkingSlot(number=4),
            ParkingSlot(number=5),
            ParkingSlot(number=6),
            ParkingSlot(number=7),
            ParkingSlot(number=8),
            ParkingSlot(number=9),
            ParkingSlot(number=10),
            ParkingSlot(number=11),
            ParkingSlot(number=12),
            ParkingSlot(number=13),
            ParkingSlot(number=14),
            ParkingSlot(number=15),
        ]

        park_slots_2 = [
            ParkingSlot(number=1),
            ParkingSlot(number=2),
            ParkingSlot(number=3),
            ParkingSlot(number=4),
            ParkingSlot(number=1),
            ParkingSlot(number=2),
            ParkingSlot(number=3),
            ParkingSlot(number=4),
            ParkingSlot(number=5),
            ParkingSlot(number=6),
            ParkingSlot(number=7),
            ParkingSlot(number=8),
            ParkingSlot(number=9),
            ParkingSlot(number=10),
            ParkingSlot(number=11),
            ParkingSlot(number=12),
            ParkingSlot(number=13),
            ParkingSlot(number=14),
            ParkingSlot(number=15),
        ]

        for car_type in car_types:
            car_type.save()

        for car_brand in car_brands:
            car_brand.save()

        for i in range(1, 10):
            car = Car(car_number=f'555{i}IM{i}', car_type=car_types[0], car_brand=car_brands[0], is_electric=False,
                      year=2000)
            car.save()

        for park in parks:
            park.save()

        for slot in park_slots_1:
            slot.save()
            slot.parking = parks[0]
            slot.save()

        for slot in park_slots_2:
            slot.save()
            slot.parking = parks[1]
            slot.save()

        return HttpResponse('Success')

    except:
        return HttpResponse('Error')


def get_cars(request):
    cars = Car.objects.all()

    return render(request, 'autopark/cars.html', {'cars': cars})


def get_car_by_id(request, car_id):
    car = Car.objects.get(id=car_id)

    brand_list = CarBrand.objects.all()
    type_list = CarType.objects.all()

    data = {                    # таким образом передали в шаблон 3 словаря:
        'car': car,
        'brands': brand_list,    # для удобства заполнения полей БРЕНДА и ТИПА в шаблоне - делаем их в виде
        'types': type_list       # выпадающего списка из всех МАРОК и ТИПОВ машин из models.py
    }
    return render(request, 'autopark/get_car_by_id.html', data)


"""
Обновляет объект автомобиля с предоставленной информацией из HttpRequest.

Параметры:
    request (HttpRequest): Объект HTTP-запроса.
    car_id (int): Идентификатор обновляемого автомобиля.

Возвращает:
    HttpResponseRedirect: Перенаправляет на URL 'get-cars' после обновления автомобиля.
"""
def update_car(request: HttpRequest, car_id: int):
    if request.method != 'POST':                      # Проверяет запрос на POST-метод. Если не POST, то возвращает ошибку
        return HttpResponse('Invalid request method')

    car = Car.objects.get(id=car_id)                   # Получаем объект автомобиля по ID

                                                       # Получаем "НОВЫЕ" ДАННЫЕ:
    car_year = request.POST.get('year')                # Года выпуска get('year'),
    car_is_electric = request.POST.get('is_electric')  # инфу является ли электрическим,
    car_type_id = request.POST.get('car_type_id')      # идентификатора ТИПА автомобиля
    car_brand_id = request.POST.get('car_brand_id')    # идентификатора БРЕНДА автомобиля из POST-запроса!!!
                                           # Почему назвали car_brand_id и car_brand_id - из Models.py -> Class Car !!!
                                                        # car_type = models.ForeignKey(CarType ...)
                                                        # car_brand = models.ForeignKey(CarBrand ...)


    car_type = CarType.objects.get(id=car_type_id)     # Находим ТИП и БРЕНД автомобиля по соотв-щим идентификаторам
    car_brand = CarBrand.objects.get(id=car_brand_id)  # т.е. получаем объекты CarType и CarBrand по ID

    car.car_type = car_type                            # Обновляем данные автомобиля по заданным полям!
    car.car_brand = car_brand
    car.year = car_year
    car.is_electric = car_is_electric == 'on'    # Для типа CHECKBOX 'on' == True (т.е. если чекбокс включен-->стоит галочка)

    car.save()                                         # СОХРАНЯЕМ изменения в БАЗЕ данных

    return HttpResponseRedirect(reverse('get-cars'))   # После сохранения перенаправляем на страницу со списком авто!!!

                                                    # reverse - возвращает "ИМЯ" URL, соответствующее указанному адресу.
                                                    # Т.е. reverse('get-cars') = '/auto-park/get-cars/'


"""
Удаляет автомобиль с заданным car_id из базы данных.

Параметры:
- request: объект HttpRequest
- car_id: int, ID удаляемого автомобиля

Возвращает:
- объект HttpResponseRedirect, перенаправляющий на URL 'get-cars'
"""
def delete_car(request: HttpRequest, car_id: int):
    car = Car.objects.get(id=car_id)
    car.delete()
    return HttpResponseRedirect(reverse('get-cars'))  # reverse - возвращает URL '/auto-park/get-cars/' по "ИМЕНИ представления"



"""
Представление для добавления нового автомобиля в автопарк.
Обрабатывает как GET, так и POST запросы.
Для GET запросов извлекает список марок и типов автомобилей и рендерит шаблон 'add_car.html' с данными.
Для POST запросов извлекает детали автомобиля из запроса и сохраняет новый автомобиль в базу данных, затем перенаправляется на URL 'get-cars'.
"""

def add_car(request):                      # Функция add_car принимает параметр request, который представляет запрос клиента
    if request.method == 'GET':               # Если запрос GET, то:
        brand_list = CarBrand.objects.all()   # функция извлекает все МАРКИ машин и их ТИПЫ
        type_list = CarType.objects.all()

        data = {                            # таким образом передали в шаблон 2 словаря:
            'brands': brand_list,           # для удобства заполнения полей БРЕНДА и ТИПА в шаблоне - делаем их в виде
            'types': type_list              # выпадающего списка из всех МАРОК и ТИПОВ машин из models.py
        }

        return render(request, 'autopark/add_car.html', data)  # функция render() возвозвращает шаблон 'add_car.html'

    if request.method == 'POST':
        car_number = request.POST.get('car_number')         # Если метод запроса равен 'POST', то функция
        car_type_id = request.POST.get('car_type_id')       # извлекает данные автомобиля из запроса POST
        car_brand_id = request.POST.get('car_brand_id')
        is_electric = request.POST.get('is_electric')
        year = request.POST.get('year')

        car_type = CarType.objects.get(id=car_type_id)
        car_brand = CarBrand.objects.get(id=car_brand_id)

        car = Car(                                          # Создаем НОВЫЙ объект Car и передаем ему данные автомобиля
            car_number=car_number,
            car_type=car_type,
            car_brand=car_brand,
            is_electric=is_electric == 'on',
            year=year
        )
        car.save()                                          # СОХРАНЯЕМ в БАЗЕ данных

        return HttpResponseRedirect(reverse('get-cars')) # После сохранения перенаправляем на страницу со списком авто!

                                                    # reverse - возвращает "ИМЯ" URL, соответствующее указанному адресу.
                                                    # Т.е. reverse('get-cars') = '/auto-park/get-cars/'


"""
Функция для поиска автомобилей по номеру, типу и бренду.

Параметры:
- request: объект HTTP-запроса

Возвращает:
- Если метод запроса 'GET', отображает шаблон 'autopark/cars.html'.
- Если метод запроса не 'GET', фильтрует объекты Car на основе строки поиска и отображает шаблон 'autopark/cars.html' 
с отфильтрованным списком автомобилей.
"""
def search_car(request):
    if request.method == 'GET':
        return render(request, 'autopark/cars.html')
    else:
        search_string = request.POST.get('search_string')
        car_list = Car.objects.filter(
            Q(car_brand__name__icontains=search_string)   # contains - поиск по "СОДЕРЖИМОМУ" строки С учетом регистра
            | Q(car_type__name__icontains=search_string)  # icontains - поиск по "СОДЕРЖИМОМУ" строки БЕЗ учета регистра
            | Q(car_number__icontains=search_string)      # НЕ забыть подключить модуль django.db.models
        )                                                 # from django.db.models import Q

        return render(request, 'autopark/cars.html', {'cars': car_list})
