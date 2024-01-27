from django.shortcuts import render
from django.http import HttpResponse
from .models import CarType, CarBrand, Car, ParkingSlot, Parking

# Create your views here.

def initialize(request):
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
