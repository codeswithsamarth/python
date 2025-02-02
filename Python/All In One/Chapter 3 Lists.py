# Python lists are containers to store set of value of any data type

friends = ["Apple","Banana",23,True,2382.002,None]

l1 = [22,44,61,11,23,9,93,1]
l1.sort()
print(l1)

l1.remove(22)
print(l1)

l1.insert(0,"Samarth")
print(l1)

l1.append(22.48)
print(l1)

l1.clear()
print(l1)

my_list = ["Samarth",124,32.23]
new_list = my_list[0:2]
print(new_list)

my_list = [30,10,20,25,30,30,30,25,25,25,25,14,25]
Twenty_Five = my_list.count(25)
Thirty = my_list.count(30)
print(Twenty_Five)
print(Thirty)

my_list2 = [22,44,55,67,45,46,77,77]
extend = [99,88,85,86,82,81,63]
my_list2.extend(extend)
print(my_list2)

my_list3 = [66,77,88,99]
print(my_list3.index(66))

My_List = [22,44,66,77,88]
My_List3 = [99,100,33,55]
Concatenation = My_List + My_List3
print(Concatenation)

my_list0 = [22,66,88,44]
print(22 in my_list0)

My_Listo = [11,22,55,66]
del My_Listo[1]
print(My_Listo)

my_list1 = [1,11,21,32]
my_list2 = [1,11,21,32]
print(my_list1 == my_list2)

my_list2.pop(1)
print(my_list2)

