class Item:
    def __init__(self, name : str,price : int,quantity = 0):

        assert price >= 0 , f"Price Cannot be zero"
        assert quantity >= 0


        # Assign to Self Object
        self.name = name
        self.price = price
        self.quantity = quantity


    def calculate_total_price(self): # Python passes the object as the first argument or parameter in Methods
        return self.price * self.quantity


item1 = Item("Phone",100,5)
print(type(item1))

print(item1.calculate_total_price())

class Items():
    def __init__(self,Name,price,quantity = 1):
        self.name = Name
        self.price = price
        self.quantity = quantity

        assert price >= 0, "Price Cannot Be less than Zero"
        assert quantity >= 0, "quantity Cannot Be less than Zero"
    def calculate_total_price(self):
        return self.price * self.quantity



items1 = Items("Laptop","1000",3)

print(items1.calculate_total_price())

