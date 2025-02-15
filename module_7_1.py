class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "Файл не найден."

    def add(self, *products):
        existing_products = set()

        try:
            with open(self.__file_name, 'r') as file:
                existing_products = {line.strip() for line in file}
        except FileNotFoundError:
            pass

        for product in products:
            product_str = str(product)
            if product_str in existing_products:
                print(f"Продукт {product} уже есть в магазине")
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(product_str + '\n')
                existing_products.add(product_str)


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
