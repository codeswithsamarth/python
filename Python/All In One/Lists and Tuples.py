# Python lists are containers to set of value of any data type

friends = ["Apple","Banana","Orange",5,345.06,False,"Aakash"]

print(friends[0]
      )
print(friends[1:4])
print(friends[3])

friends.append("Harry")
friends.append(99)
print(friends)

lists = [11,9,2,3,4,1,0,99,88]
# lists.sort()
print(lists.reverse())
print(lists)

l1 = ["Samarth","Harshit","Sanket",]
l1.insert(-1,"Aa")
print(l1)

value = l1.pop(0)
print(value)
print(l1)

l1.remove("Aa")
print(l1)

l1.clear()
print(l1)


my_list = [1,2,3,4,5]
new_list = my_list[0:4]
print(new_list)

my_list = [1,2,3,4,5]
new_lists = my_list.copy()
print(new_lists)

my_list2 = [11,22,33,33,3,3,33,33,33,33]
print(my_list2.count(33))

my_list1 = [1,22,33,44,55]
my_list1.extend([66,77,88])
print(my_list1)

my_list9 = [1,2,3,4]
print(my_list9.index(3))

my_list99 = [1,2,3,4,5,6]
my_list999 = [7,8,9,10,11]
new_lists99 = my_list99 + my_list999
print(new_lists99)

my_listo = [1,2,3,4,5,6]
print(1 in my_listo)

del my_listo[1]
print(my_listo)

my_listo = [1,2,3,4,5]
new_lists = my_list.copy()
print(my_listo == new_lists)

# indexing slicing append sort reverse insert remove clear copy extend count index function concentation of lists contains membership delete equ = equ


# Tuples in Python

# Tuple is an ordered immutable data type in python

tuple = ()
print(type(tuple))

tuple = (1,45,65,"Rohan",65,784)

a = tuple[0]
print(tuple)

a = tuple[1:]
print(a)

tuple1 = (11,22,33,44)
tuple2 = (55,66,77,88)
tuple3 = tuple1 + tuple2
print(tuple3)

my_tuple = (11,22,99,0,24,11,1,1,1,1,1,1,1,1)
rep_tuple = my_tuple * 3
print(rep_tuple)

print(len(my_tuple))

print(11 in my_tuple)

print(my_tuple.count(1))

my_tuplew = (11,22,33,44,55)
print(my_tuplew.count(11))

