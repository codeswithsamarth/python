name = "Harry"
# Slicing in python
print(name[0:3])#start from index 0 for all the way till 3 except
character1 = (name[1])
print(character1)
print(len(name))

print(name[-4: -1])
print(name[1:4])
print(name[:4])#is same as print(name[0:4])
print(name[1:]) #is same as print(name(1:5) till length

#skip value

name2 = "amazing"#n
word = name2[1:6:2]#mzn

a = "0123456789" #count till 7 not include 7 means count till six
x = a[1:7:3]
print(x)

b = "abcdefghijklmnopqrstuvwxyz" #till 8 =j bfj
b1 = b[1:9:4]

# advanced indexing & slicing
my_string = "Python"
print(my_string[0])
print(my_string[3])
print(my_string[-1])
print(my_string[-3])

# Basic Slicing

my_string1 = "JavaSpringBoot"
print(my_string1[0:3])
print(my_string1[2:5])

#Start And End

my_stringm = "JavaScript"
print(my_stringm[:3])
print(my_stringm[3:])


# Negative Slicing
Webd = "HtmlCss"
print(Webd[:-1])
print(Webd[-3:])
print(Webd[-1:])

#Slicing With Step
fullstack = "JavaPython"
print(fullstack[::2])
print(fullstack[::-1])
print(fullstack[3::])

#
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[::3])

letters = "abcdefghij" #till g bdf
print(letters[1:6:2])
print(letters[::-1])
print(letters[1::3])


my_list = [1,2,3,4,5,6,7,8,9,10]#3,8
print(my_list[-4::-2])


