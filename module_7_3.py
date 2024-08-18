# Задача "Найдёт везде"

class WordsFinder:
    def __init__(self, *file_names):
        # Записываем переданные имена файлов в атрибут file_names в виде списка
        self.file_names = list(file_names)

    # Подготовительный метод get_all_words, который возвращает словарь вида:
    # {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
    # 'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов
    # ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле
    def get_all_words(self):
        # Создаем пустой словарь all_words, в который будем записывать полученные данные после обработки файлов
        # (ключ - название файла, значение - список из слов этого файла)
        all_words = {}
        # Указываем список символов пунктуации, которые будем убирать из текста
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:

            with open(file_name, 'r', encoding='utf-8') as file:
                # Читаем в переменную text содержимое файла и переводим его содержимое в нижний регистр
                text = file.read().lower()

                # Избавляемся от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке
                # Разбиваем полученную строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
                for symbol in punctuation:
                    text = text.replace(symbol, "")
                words = text.split()

                # Записываем полученные данные (список слов) в словарь all_words
                all_words[file_name] = words

        return all_words

    # Метод find, где word - искомое слово. Возвращает словарь,
    # где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла
    def find(self, word):
        # Переводим искомое слово word в нижний регистр с помощью метода lower() для правильного поиска
        word = word.lower()

        # Формируем словарь со списком всех слов во всех имеющихся файлах
        all_words = self.get_all_words()

        # Словарь, содержащий результат первого вхождение слова word в каждом файле
        result = {}

        # Перебираем файлы и списки слов с помощью метода items()
        for file_name, words in all_words.items():

            # Если искомое слово word найдено, в словарь result добавляем пару
            # {имя_файла: позиция_найденного_слова}
            if word in words:
                # Находим первую позицию найденного слова в списке слов words
                result[file_name] = words.index(word) + 1
            else:
                # Если слово word не найдено
                result[file_name] = None

        return result

    # Метод count, где word - искомое слово. Возвращает словарь,
    # где ключ - название файла, значение - количество слов word во всем списке слов этого файла
    def count(self, word):
        # Переводим искомое слово word в нижний регистр с помощью метода lower() для правильного подсчета
        word = word.lower()

        # Формируем словарь со списком всех слов во всех имеющихся файлах
        all_words = self.get_all_words()

        # Словарь, содержащий число вхождений слова word в каждом файле
        result = {}

        # Перебираем файлы и списки слов с помощью метода items()
        for file_name, words in all_words.items():
            # Подсчитываем количество вхождений слова word во всем списке слов полученного из файла file_name
            result[file_name] = words.count(word)

        return result


# Пример выполнения программы:

finder1 = WordsFinder('test_file.txt', )
print(finder1.get_all_words())
print(finder1.find('ChILd'))
print(finder1.count('Child'))
