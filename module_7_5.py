# Задание по теме "Файлы в операционной системе"

import os
import time

# Переменная directory с путем к каталогу
directory = r".\DIR"

# Обход каталога с помощью os.walk
for root, dirs, files in os.walk(directory):
    for file in files:
        # Получаем полный путь к файлу
        filepath = os.path.join(root, file)

        # Подучаем время последней модификации файла
        filetime = os.path.getmtime(filepath)

        # Получаем время изменения файла
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # Получаем размер файла
        filesize = os.path.getsize(filepath)

        # Получаем родительскую директорию файла
        parent_dir = os.path.dirname(filepath)

        # Получаем информацию о файле

        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},'
              f' Родительская директория: {parent_dir}')
