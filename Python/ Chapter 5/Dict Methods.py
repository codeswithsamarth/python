marks = {
    "Harry": 100,
    "Shubam": 56,
    "Rohan": 23,
    0: "Harry"
}

marks1 = {
    "Harshit": 100,
    "Sanket": 78,
    "Rohan": 67,
    0: "Joker"
}
print(marks1.items())
print(marks.keys())
print(marks.values())
print(marks1.update({"Harshit": 99,"Renuka":90}))
print(marks1)
print(marks1.get('Harshit2'))
# print(marks1["Harshit2"])
print(marks)

final_marks = marks.copy()
print(final_marks)

#The dict.fromkeys() method creates a new dictionary with keys from a given sequence
new_dict = marks1.fromkeys('a',"Sanket")
print(new_dict)

keys = ['a','b','c']
my_dict = dict.fromkeys(keys,0)
print(my_dict)
items = ["apple","banana","orange","apple","banana","apple"]
item_count = dict.fromkeys(set(items),0)
for item in items:
 item_count[item] +=1
print(item_count)


categories = ['itGroceries', 'Utilities', 'Rent', 'Entertainment', 'Transportation']

expenses = dict.fromkeys(categories, 0)

print("Initial Expenses:")
for category, amount in expenses.items():
    print(f"{category}: ${amount}")

expenses['Groceries'] += 50  # Adding $50 to Groceries
expenses['Utilities'] += 100  # Adding $100 to Utilities
expenses['Entertainment'] += 20  # Adding $20 to Entertainment

print("\nUpdated Expenses:")
for category, amount in expenses.items():
    print(f"{category}: ${amount}")

my_dict2 = {'a':1,'b':2,'c':3}
value = my_dict2.pop('b')
print(my_dict2)
print(value)
value = my_dict2.pop('d','Not Found')
print(value)
print(my_dict2)

my_dict = {'a': 1, 'b': 2, 'c': 3}
key, value = my_dict.popitem()
print(f"removed item : ({key}),({value})")
print(f"updated dictionary : ",my_dict)

my_dict = {'a': 1, 'b': 2}
value = my_dict.setdefault('a',10)
print(value)
print(my_dict)
value2 = my_dict.setdefault('c',10)
print(value2)
print(my_dict)


# Dictionary
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Harry": 99,"Renuka": 100})
# print(marks)

# print(marks.get("Harry2"))# Gives None
# print(marks["Harry2"])
# # Chatgpt
# marks.clear()
# print(marks)
# new_marks = marks.copy()
# print(new_marks)

#The dict.fromkeys() method creates a new dictionary with keys from a given sequence
# new_dict = marks.fromkeys("a","Sanket")
# print(new_dict)

# keys = ['a','b','c']
# my_dict = dict.fromkeys(keys,0)
# print(my_dict)

# items = ["apple","banana","orange","apple","banana","apple"]
# item_count = dict.fromkeys(set(items),0)
# for item in items:
#     item_count[item] +=1
#     print(item_count)






#

# Pop Methods
# my_dict2 = {'a':1,'b':2,'c':3}
# value = my_dict2.pop('b')
# print(value)
# print(my_dict2)
# value = my_dict2.pop('d','Not Found')
# print(value)
# print(my_dict2)

# Pop items
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# key, value = my_dict.popitem()
# print(f"removed item : ({key}),({value})")
# print(f"updated dictionary : ",my_dict)

# Set deafult
#If the key exists in the dictionary, setdefault() simply returns its value.
# my_dict = {'a': 1, 'b': 2}
# value = my_dict.setdefault('a',10)
# print(value)
# print(my_dict)

# my_dict = {'a': 1, 'b': 2}
# value = my_dict.setdefault('c', 3)
# print(value)
# print(my_dict)

