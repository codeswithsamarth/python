# Encapsulation
"""Restricting to ability to over_ride the values for the object """
"""Encapsulation restricts direct access to an object prevent external 
override of value and allow to control them through methods"""


from item import Item

item1 = Item("MyItem",750)
item1.apply_bonus(0.2)

print(item1.price)

item2 = Item("My_Phone",90000)
item2.apply_tax()
print(item2.price)

Trader = Item("Nifty50",540000)
Trader.Tax_on_Trading()
print(Trader.price)

# Abstraction is the concept of simplifying system by exposing essential feature
# while hiding unnecessary details from users

Item1 = Item("My_Item",900,8)
Item1.send_email()

from phone import Phone

item1 = Phone("Jscphone",800,99)
item1.Tax_on_Trading()
print(item1.price)

# Polymorphism refers Many Forms

from keyboard import keyboard

