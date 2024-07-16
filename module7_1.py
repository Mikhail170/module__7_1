class Product:
    def __init__(self, name: str, weight: float, category: 'str'):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self, __file_name):
        self.__file_name = '../text_files/practics/products.txt'

    def get_products(self):
        '''метод открывает файл products в режиме чтения, считывает данные
        находящиеся в нем, закрывает файл и возвращает все, что считано в
        этом файле'''
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        '''Открывает инкапсулированный файл в режиме добавления неограниченного количества объектов Product,
        вводит переменную которая равна данным из списка, проходит циклом for
        по этим данным из файла, и если имя продукта не совпадает с одним из имен
        находящимся в файле - добавляет его в этот файл, если имя продукта
        уже в нем есть, то выдает сообщение ... и закрывает файл'''
        file = open(self.__file_name, 'a')
        product_list = self.get_products()
        for product in products:
            if product.name not in product_list:
                file.write(str(product) + '\n')
            else:
                print(f'Продукт {product.name} уже добавлен в магазин')
        file.close()


s1 = Shop('../text_files/practics/products.txt')
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
p4 = Product('orange', 6.5, 'Fruits')

print(p2)
print(s1.get_products())
s1.add(p1, p2, p3, p4)
