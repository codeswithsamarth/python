s1 = {1,2,3}
s2 = {3,2,4}
union = s1|s2
print(union)
print(s1.union(s2))

# Intersection Returns common value from both side

si = {11,22,33,99,66,55}
so = {11,22,33,44,55,66,77}
intersection = si & so
print(intersection)

# difference self set

s1 = {1,2,3,4}
s2 = {2,4,6}

difference = s1-s2
difference_second = s2-s1
print(f"The Value Which Not Present in Second {difference}")

# Symetric != Other Set

sw = {1,2,3}
swq = {2,3,4}
symmetric = sw^swq
print(symmetric)

s0 = {1,2,3}
s11 = {1,2,3,4,5}

if s0 <= s11:
    print(f"The {s0} is a subset of {s11}")
else:
    print(f"The {s0} is Not a subset of {s11}")


s1 = {1,2,3}
s2 = {2,3,4}
print("Before",s1)
s1 ^= s2
print("After",s1)

# As it is signs and equal to for updates
