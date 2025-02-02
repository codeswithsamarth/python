friends = ["Apple","Orange",5,345.06,False,"Aakash","Rohan"]
print(friends)
friends.append("Harry")
print(friends)
# Sorting (Ascending Order)
l1 = [1,33,22,66,55,82]
# l1.sort()
# # Reverse (Descending Order)
# print(l1)
# l1.reverse()
# # Inserting
# l1.insert(3,3333) # Insert 3333 such that its index in the list 3
# print(l1)
#Pop
value = l1.pop(3)
print(value)
print(l1)
# Remove Method
l1.remove(55)
print(l1)
# Clear
# l1.clear()
# print(l1)

# Copy
my_list = [1,2,3]
new_list = my_list.copy()
print(new_list)
# ---------------
my_list.copy()
print(my_list)

# Count
my_list2 = [1,2,3,4,5,6,6,6,6]
print(my_list2.count(6))

# Extend
my_list1 = [1,2,4]
my_list1.extend([4,5,6])
print(my_list1)

my_list9 = [1,2,3,4]
print(my_list9.index(3))

# Concatenation of Lists
my_list99 = [12,24,36,48,60]
new_list99 = my_list99 +  [72,84,96,108,120]
print(new_list99)

# Contains
my_Listo = [1,11,21,32]
print(11 in my_Listo)

# delitem deletes an element at specific index
my_Listo = [1,11,21,32]
del my_Listo[1]
print(my_Listo)

# equal == eq
my_Listo = [1,11,21,32]
other_listo = [1,11,21,32]
print(my_Listo == other_listo)


