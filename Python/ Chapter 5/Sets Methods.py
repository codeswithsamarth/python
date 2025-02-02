s = {1,5,32,54,5,5,"Harry"}
print(s,type(s))
d = set()
d.add(55)
print(d)
# Properties of sets
# 1. Sets are unordered => Element’s order doesn’t matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets cannot contain duplicate values.

d1 = {'a':1,'b':2}
print(len(d1))

# Operations on Sets
s = {1,8,2,3}
print(len(s))
s.remove(1)
print(s)
a = s.pop()
print(s)


# Promt Method

# Add
s = {1,2,3}
s.add(4)
print(s)

# Remove
s = {1,2,3,4}
s.remove(2)
print(s)

# Discard Removes an element if there
sd = {1,2,3,4}
sd.discard(4)
print(sd)

# Pop
sp = {1,2,3}
element = sp.pop()
print(element)
print(sp)

# Clear
clear = {1,2,3,4}
clear.clear()
print(clear)

# Union Return a new sets with all element from both side
s1 = {1,2,4}
s2 = {2,3,4,}
print(s1.union(s2))

# Intersection Returns a new set with element common to both sides
si = {11,22,33,99,66,55}
so = {11,22,33,44,55,66,77}
print(si.intersection(so))

# Difference Return a new Set with Different element in the current set but not in other set
s1 = {1,2,3,4}
s2 = {2,4,6}
print(s1.difference(s2))
print(s2.difference(s1))

# Symmetric difference Return a new Set which Element not present each there lists
sw = {1,2,3}
swq = {2,3,4}
print(swq.symmetric_difference(sw))

# Copy
s9 ={1,2,3}
new_set = s.copy()
print(new_set)

# Subset Returns Bool if all element of the sets in other sets
s0 = {1,2,3}
s11 = {1,2,3,4,5}
result = s0.issubset(s11)
print(result)

# Superset Return Bool if all elements of other set in the set
s1 = {1,2,3}
s2 = {2,3}
results = s1.issuperset(s2)
print(results)

# isdisjoint Returns Bool if set has no common value
sq = {1,2,5}
sw = {3,4,}
result_final = s1.isdisjoint(s2)
print(result_final)

s1 = {1,2,3}
s2 = {2,3,4}
print("Before",s1)
s1.symmetric_difference_update(s2)
print("After",s1)

s1 = {1,2,3}
s2 = {2,3,4}
s3 = {3,4,5}

print("Before",s2)
s2.intersection_update(s3)
print("After",s2)

s1 = {1,2,3}
s2 = {2,3,4}
print("Before",s1)
s1.difference_update(s2)
print("After",s1)

s1 = {1,2}
s2 = {2,3}
s3 = {3,4}
print("Before",s1)
s1.update(s2,s3)
print("After",s1)

s1 = {22,44,66,88}
s2 = {12,22,44,66}
print("Before",s1) # s1 22,44,66,88
s1.symmetric_difference_update(s2)
print("after",s1) # 12 88

s21 = {14,28,42,56,70}
s22 = {14,28,70,56,112}
print("Before",s21)
s21.symmetric_difference_update(s22)
print("After",s21)

s1 = {11,22,33}
s2 = {33,44,55}
s3 = {55,66,77}

print("Before",s1)
s1.intersection_update(s2,s3)
print("After",s1)

s1 = {11,22,33,44}
s2 = {12,22,44,66}
print("Before",s1)
s1.difference_update(s2)
print("After",s1)

s1 = {7,14,21,28,35}
s2 = {7,14,21,28,35,42,49}
s3 = {7,14,21,28,35,42,49,56}
s4 = {7,14,21,28,35,42,49,56,63,70}

sorted_set = sorted(s1)
print(sorted_set)

print("Before",s1)
s1.update(s2,s3,s4)
print("After",s1)