from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import UploadedFile

# Create your views here.


def upload_file(request):
    if request.method == 'POST':                    # Проверяет запрос на POST-метод. Если не POST, то возвращает ошибку
        my_file = request.FILES['myfile']           # Загружаем файл
        uploaded_file = UploadedFile(file=my_file)  # Создает объект UploadedFile с загруженным файлом
        uploaded_file.save()                        # Сохраняет объект в БД
        return HttpResponseRedirect(reverse('get-cars'))
