# Tuple are ordered and immutable data type in python

tup = (33,55,666,777,23,33)

# There are only two methods for tuple
a = tup.count(33)
print(a)

b = tup.index(55)
print(b)

# Accessing element
my_tuples = (1,2,3)
print(my_tuples[0])

my_tuples2 = (2,4,5,6,7,8)
print(my_tuples2[::2])

tup1 = (1,3,5)
tup2 = (7,9,11)
tup3 = tup1 + tup2
print(tup3)

my_tuple1 = (1,2,3)
rep_tuple = my_tuple1 * 3
print(rep_tuple)

print(len(my_tuple1))

my_tuples3 = (1,2,4)
print(2 in my_tuples3)

my_tuple1 = (1,2,3)
for item in my_tuple1:
    print(item)

maxed = (1,2,3)
print(max(maxed))

print(min(maxed))
print(sum(maxed))
print(sorted(maxed))

nine = (77,22,33,66,44,55)
print(any(nine))

nine9 = (9,9,9,9,9)
print(all(nine9))

fruits = []
f1 = input("Enter Fruits Name:")
fruits.append(f1)
f2 = input("Enter Fruits Name:")
fruits.append(f2)
f3 = input("Enter Fruits Name:")
fruits.append(f3)
f4 = input("Enter Fruits Name:")
fruits.append(f4)
f5 = input("Enter Fruits Name:")
fruits.append(f5)
f6 = input("Enter Fruits Name:")
fruits.append(f6)
f7 = input("Enter Fruits Name:")
fruits.append(f7)
f8 = input("Enter Fruits Name:")
fruits.append(f8)

print(fruits)



