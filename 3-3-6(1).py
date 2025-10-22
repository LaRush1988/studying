class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
    
    def get_basic_info(self):
        return f'{self.name} (в наличии: {self.quantity})'
    
    def get_full_info():
        pass

class Kettlebell(Product):

    def __init__(self, name, quantity, weight):
        super().__init__(name, quantity)
        self.weight = weight

    def get_full_info(self):
        return f'{self.name} (в наличии: {self.quantity}). Вес: {self.weight} кг'
    
class Clothing(Product):

    def __init__(self, name, quantity, size):
        super().__init__(name, quantity)
        self.size = size
    
    def get_full_info(self):
        return f'{self.name} (в наличии: {self.quantity}). Размер: {self.size}'
    
    # Для проверки вашего кода создадим пару объектов...
small_kettlebell = Kettlebell('Гиря малая', 15, 2)
shirt = Clothing('Футболка', 5, 'L')

# ...и вызовем их методы:
print(small_kettlebell.get_full_info())
print(shirt.get_full_info())