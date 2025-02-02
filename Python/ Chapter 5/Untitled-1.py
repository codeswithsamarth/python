
class Item:
    def calculate_total_price(self,price,quantity):
        return price * quantity

item1 = Item
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.quantity,item1.price))


















































