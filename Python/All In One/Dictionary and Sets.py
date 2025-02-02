# Dictionary is a collection of keys-value pairs.


marks = {
    "Samarth":98,
    "Harry":97,
    "Shubham":96,
    "Rohan":46
}

print(marks,type(marks))


print(*marks.items())

print(marks.keys())
print(marks.values())

marks1 = {
    "Harshit": 100,
    "Sanket": 78,
    "Rohan": 67,
    0: "Joker"
}
marks1.update({"Harshit":99,"Harshit":89})
print(marks1)

print(marks1.get("Has"))

final_marks = marks1.copy()
print(final_marks)

items = ["Samarth","Sanket","Harahi","Harshit"]*100
item_count = dict.fromkeys(set(items),0)
for item in items:
    item_count[item] += 1
    print(item_count)

my_dict2 = {'a':1,'b':2,'c':3}
key = my_dict2.pop('b')
print(my_dict2)

marks_dict = {"Samarth":98,"zaid":99}
keys, values = marks_dict.popitem()
print(f"{keys},{values}")


my_dict = {'a':1,'b':2}
a = my_dict.setdefault('c',10)
print(a)
print(my_dict)


d = {}
e = set()
print(type(e))
s = {1,5,23,88}
print(s)

# Set is a unordered collection of non-repetitive elements.

s1 = {11,22,33,44,55}
s1.add(99)
print(s1)


s1.remove(99)
print(s1)

a = s1.pop()
print(a)

a = s1.pop()
print(a)

sd = {1,2,3,4}
sd.discard(9)
print(sd)


clear = {1,2,3,4}
clear.clear()
print(clear)

# Union Return a new sets with all element from both side
s1 = {1,2,4}
s2 = {2,3,4}
print(s1.union(s2))

si = {11,22,33,44,55,66,77,88}
so = {55,66,77,88,99}
print(si.intersection(so))


# Difference Return a new Set with Different element in the current set but not in other set
s1 = {1,2,3,4}
s2 = {2,4,6}
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))


current = {11,22,33,44}
new = current.copy()
print(new)


# Subset Returns Bool if all element of the sets in other sets
s0 = {1,2,3}
s1 = {1,2,3,4,5,6}
print(s0.issubset(s1))

s2 = {1,2,3,4,5}
s3 = {2,3,4}
print(s2.issuperset(s3))


sq = {1,2,5}
sw = {3,4}
result_final = sq.isdisjoint(sw)
print(result_final)

s1 = {1,2,3}
s2 = {2,3,4}
print("Before",s1)
s1.symmetric_difference_update(s2)
print("After",s1)

s2 = {3,5,7,9}
s3 = {7,9}
print("Before",s2)
s2.symmetric_difference_update(s3)
print("After",s2)

s1 = {1,2,3}
s2 = {2,3,4}
s3 = {3,4,5}
print("Before",s1)
s1.intersection_update(s2,s3)
print("After",s1)

s1 = {1,2,3}
s2 = {2,3,4}
print("Before",s2)
s2.difference_update(s1)
print("After",s2)

s1 = {7,14,21,28,35}
s2 = {42,49,56,63,70}
print("Before",s1)
s1.update(s2)
print("After",s1)
print(sorted(s1))

