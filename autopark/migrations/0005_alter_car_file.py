# Generated by Django 5.0.1 on 2024-03-16 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autopark', '0004_alter_car_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='file',
            field=models.FileField(default=1, upload_to='', verbose_name='car_file/'),
            preserve_default=False,
        ),
    ]