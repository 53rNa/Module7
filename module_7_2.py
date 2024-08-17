# Задача "Записать и запомнить"

def custom_write(file_name, strings):
    file = open(file_name, 'w')

    strings_positions = {}

    # Просматриваем список strings, отслеживая номер строки (i) и саму строку (line)
    # i — номер строки, нумерацию ставим с 1 (параметр start=1)
    # line — текущая строка из списка strings
    for i, line in enumerate(strings, start=1):
        position = file.tell()   # Получаем номер байта начала строки
        file.write(line + '\n')  # Записываем строку с новой строки в файл

        # Добавляем запись в словарь strings_positions
        # Ключ — кортеж из номера строки и номера байта начала строки (i, position)
        # Значение — строка line, которую записали в файл
        strings_positions[(i, position)] = line
    return strings_positions

    file.close()

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('example.txt', info)
for elem in result.items():
    print(elem)