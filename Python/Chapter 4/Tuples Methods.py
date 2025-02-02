a = (1,45,65,"Rohan","65",784)
print(type(a))

# Accessing Elements
my_tuple = (1,2,3)
print(my_tuple[0])

# Slicing
my_tuples = (1,2,3,4,7,9,17,22)
print(my_tuples[::2])

# Concatenation
tuple1 = (1,2,3,4)
tuple2 = (5,6,7,8)
tuple3 = tuple1 + tuple2
print(tuple3)

# repetition
my_tuple1 = (1,2,3)
rep_tuple = my_tuple1 * 3
print(rep_tuple)

# Length
my_tuple1 = (1,2,3)
print(len(my_tuple1))

# Membership
my_tuple2 = (1,2,3)
print(2 in my_tuple2)

# Loop In Tuples
my_tuple1 = (1,2,3)
for item in my_tuple1:
    print(item)
# Count
my_tuple12 = (1,2,2,2,2,2)
print(my_tuple12.count(2))

# Index
my_tuple13 = (1,2,3,54,21)
print(my_tuple13.index(2))

my_tuples13 = (1,2,3)
a,b,c = my_tuples13
print(a,b,c)