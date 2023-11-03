# Contructor, __init__
class Item():
    def __init__(self, name: str, price: float, quantity=0):
        #print(f'Tushar {name}')
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item('phone', 200, 5)
item2 = Item('laptop', 500, 3)
# commenting out

print(item1.calculate_total_price())
print(item2.calculate_total_price())