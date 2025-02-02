# item1 = "Phone"
# item1_price = 100
# item1_quantity = 5
# item1_price_total = item1_price * item1_quantity
#
# print(type(item1))
# print(type(item1_price))
# print(type(item1_quantity))
# print(type(item1_price_total))

class Item:
    def __init__(self,name:str,price:int,quantity = 0): # The Action Will Done On Every Instances
        self.name = name # Dynamic Attribute assignment
        self.price = price
        self.quantity = quantity
        assert price >= 0, f"Price Must Be Greater Than 0"
        assert quantity >= 0, f"Quantity Must be Greater Than 0"
    def calculate_total_price(self): # Python Passes The object As the First Argument
            return self.price * self.quantity


item1 = Item("Phone",100,)
item2 = Item("Laptop",1000,)
print(item1.price)
print(item1.quantity)

print(item1.calculate_total_price())
print(item2.calculate_total_price())


# Problem1 = To create Each Item To Create Attribute Solu = __init__(intentionally / Constructor)
"""Problem2 = If We Pass Int Instead Of String In Following Code Based To 17 18 Line Its Repeated The String That
To avoid It (Assert)"""


class Revision:

    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        assert price >= 0,f"Price be greater than Zero"
        assert quantity >= 0,f"Quantity Must be Greater Than Zero"




    def calculate_total_price(self):
        return self.price * self.quantity

item3 = Revision("Mackbook",900,5)

item3.quantity = 9
print(item3.name)
print(item3.price)

item4 = Revision("Xyz",1400,7)

a = item4.calculate_total_price()
b = item3.calculate_total_price()
print(a)
print(b)


# Problem1 = To create Each Item To Create Attribute Solu = __init__(intentionally / Constructor)
"""Problem2 = If We Pass Int Instead Of String In Following Code Based To 17 18 Line Its Repeated The String That
To avoid It (Assert)"""

# item1 = "Phone"
# item1_price = 100
# item1_quantity = 5
# item1_total = item1_price * item1_quantity
#
# l1 = [item1_price,item1_total,item1_quantity,item1]
# types = list(map(lambda x: type(x),l1))
# print(types)
#
"""
about class attribute The Attribute can be accessed globally This Belong to The class
"""

import csv
class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self,name,price,quantity = 0):
        self.name = name
        self.quantity = quantity
        self.price = price

        assert price > 0, f"Price Must be Greater Than Zero"
        assert quantity >= 0,f"quantity be greater Than Zero"

        Item.all.append(self)

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item({self.name}),({self.price}),({self.quantity})"

    @classmethod
    def instantiate_from_csv(cls): # When Class Method is called Class Object passed as First Argument
        with open('items.csv','r') as f: # F = code Which Can be read as f
            reader = csv.DictReader(f) # Read Item and Return In Dictionary
            items = list(reader)
        for item in items:
            Item(
            name = item.get('name'),
            price = float(item.get('price')),
            quantity = int(item.get('quantity'))

            )
    @staticmethod
    def is_integer(num):
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False


print(Item.is_integer(22))


"""If We use Static Method As Cookie Cutter It does Not think about any Cookie
It Just Help without Looking Shape And Size It Does Not Information from Specific Object or Instances
"""
class cookie_cutter():
    pass
cookies = cookie_cutter()
cookies.shape = "Circle"
cookies.size = 30

