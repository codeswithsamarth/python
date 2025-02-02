import csv
class Item:
    pay_rate = 0.8
    all = []
    instance_count = 0
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
        Item.instance_count += 1
        assert price >= 0, f"Price Cannot be less than 0"
        assert quantity >= 0, f"quantity Can't be Zero or Less than Zero"
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name} {self.price} {self.quantity})"

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv")as f:
            reader = csv.DictReader(f)
            item = list(reader)
            for items in item:
                Item(
                name= items.get("name"),
                price= float(items.get("price")),
                quantity= int(items.get("quantity"))
            )
"""
class Method is a method than can access class level attribute or modify class level attribute
it can only called by class Itself not by instances

they are used for manipulate different structure of data to instantiate data object
like instantiating objects from csv

"""
# Item.instantiate_from_csv()
# print(Item.all)

"""
Static Method is a Method In Python defined with a Class Doesn't depend on any instance
In Simple Way Static Method Does Not require any information From Instance It directly
Do a Task Assigned to It

If We use Static Method As Cookie Cutter It does Not think about any Cookie
It Just Help without Looking Shape And Size It Does Not Information from Specific Object or Instances 
"""

class Phone(Item):
    def __init__(self,name,price,quantity = 0,broken_phone = 0):
        super().__init__(name,price,quantity)
        assert broken_phone >= 0,f"quantity Can't be Zero or Less than Zero"
        self.broken_phone = broken_phone

phone1 = Phone("TrialPhone1",900,7)
phone2 = Phone("TrialPhone2",750)
print(phone1.calculate_total_price())

