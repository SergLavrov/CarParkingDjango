from django.db import models

# Create your models here.

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')  # информация о загруженном файле
    uploaded_at = models.DateTimeField(auto_now_add=True) # дата и время загрузки


# 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
# 2) Quit and manually define a default value in models.py.
# Select an option:

