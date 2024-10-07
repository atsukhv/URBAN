class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'Название: {self.name}, вес: {self.weight}, категория: {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            return file.readlines()

    def add(self, *products):
        read_file = self.get_products()
        file = open(self.__file_name, 'a')

        existing_products = [line.strip() for line in read_file]

        for product in products:
            product_str = str(product).strip()
            if product_str not in existing_products:
                file.write(f'{product_str}\n')
            else:
                print(f'Продукт {product.name} уже есть в магазине')

        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(*s1.get_products())
