# Задача "Учёт товаров"

class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name                  # название продукта(строка)
        self.weight = weight              # общий вес товара (дробное число) (5.4, 52.8 и т.п.)
        self.category = category          # категория товара (строка)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self) -> str:
        self.__file_name = 'products.txt'

    def get_products(self) -> str:
        file = open(self.__file_name, 'r')
        return file.read()
        file.close()

    def add(self, *products: Product):

        current_products_in_file = self.get_products()

        # Используем множество, т.к. оно исключает одинаковые названия продуктов для проверки их по названнию
        existing_product_names = set()

        # Извлекаем имена продуктов из содержимого файла со списком продуктов, а existing_product_names
        # будет указывать на множество всех названий продуктов, которые уже есть в файле.
        if current_products_in_file:
            existing_product_names = {line.split(',')[0].strip() for line in current_products_in_file.splitlines()}

        # Добавляем в файл __file_name каждый продукт из products, если его ещё нет в этом файле (по названию).
        # Если такой продукт уже есть в данном файле, то не добавляем и выводим строку
        # 'Продукт <название> уже есть в магазине'
        file = open(self.__file_name, 'a')
        for product in products:
            if product.name not in existing_product_names:
                existing_product_names.add(product.name)
                file.write(str(product) + '\n')
            else:
                print(f'Продукт {product.name} уже есть в магазине')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')   # не будет добавлен в файл, т.к. продукт с таким
                                                                 # названием уже есть в магазине
p4 = Product('Груша', 8.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3, p4)

print()
print(s1.get_products())