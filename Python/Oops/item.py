import csv
class Item:
    pay_rate = 0.8
    all = []
    instance_count = 0
    def __init__(self,name,price,quantity=0):
        self.__name = name
        self.__price = price
        self.quantity = quantity
        Item.all.append(self)
        assert price >= 0, f"Price Cannot be less than 0"
        assert quantity >= 0, f"quantity Can't be Zero or Less than Zero"
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name} {self.__price} {self.quantity})"

    def calculate_total_price(self):
        return self.__price * self.quantity


    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_bonus(self,increment_value):
        self.__price = self.__price + self.__price * increment_value

    def apply_tax(self,tax = 0.06,increment = 0.12):
        self.__price = self.__price - self.__price * tax - self.__price * increment

    def Tax_on_Trading(self):
        self.__price = self.__price - self.__price * 0.15

    def __connect_to_server(self):
        pass

    def __body(self):
        return (f"We Have Order as Per Your Request {self.__price} {self.quantity} Times At Discounted Rate"
                f"Samarth Patil")

    def __send(self):
        pass

    def send_email(self):
        self.__connect_to_server()
        self.__body()
        self.__send()



    @name.setter
    def name(self,value):
        if len(value) >= 10:
            print("Length of Attribute is too long")
        else:
            self.__name = value

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

"""
Static Method is a Method In Python defined with a Class Doesn't depend on any instance
In Simple Way Static Method Does Not require any information From Instance It directly
Do a Task Assigned to It

If We use Static Method As Cookie Cutter It does Not think about any Cookie
It Just Help without Looking Shape And Size It Does Not Information from Specific Object or Instances 
"""




