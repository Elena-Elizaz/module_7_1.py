class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        str_roduct = (f"{self.name}, {self.weight}, {self.category}")
        return  str_roduct



class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name, 'r+' )
        prod_str = file.read()
        file.close()
        return prod_str

    def add(self, *products):
        fil_get = self.get_products()
        for i in products:
            if i.name not in fil_get:
                file = open(self.__file_name, 'a')
                file.write(f'{i}\n')
                file.close()
            else:
                print(f'Продукт {i.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')



s1.add(p1, p2, p3)

print(s1.get_products())