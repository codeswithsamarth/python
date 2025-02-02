# Oops

# item1 = "Phone"
# item1_price = 100
# item1_quantity = 5
#
# # In above Code Its Look That these Variable are connected with each Other
# # Because they Start With Same Prefixes
#
# print(type(item1))

class Item:
    pass

item1 = Item() # Create Instances of A class

# Assign Attribute to the Class

# Each Attribute Assigned to a Class
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

print(type(item1))

# ____________________

class Items_:
    def calculate_total_price(self,x,y):
        return x + y
item2: Items_ = Items_()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
a = item2.calculate_total_price(item2.quantity,item2.price)
print(a)

# For each Item We need to create Attribute To Avoid We Use constructor(__init__)

class Itemsp:
    pay_rate = 0.8

    def __init__(self,Name,price,quantity):
        self.name = Name
        self.price = price
        self.quantity = quantity

    item1 = Items()

    item1 = Item("Phone", 5, )  # Creating Instances of a Class

    item2 = Item("Laptop", 8, )
