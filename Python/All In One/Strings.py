# String is a sequence of characters enclosed in quotes.
# Sting is a data type in Python

name = "Samarth"
print(name[1]) # Index Starts from 0
print(name[0:3]) # From Zero Till 2

print(len(name))

print(name[-4:-1])
print(name[1:4])

print(name[:4])
print(name[1:])

name2 = "amazing" # Till n
word = name2[0:6:2]
print(word)

a = "0123456789"
print(a[1:7:3])

b = "zxcvbnmlkjhgfsdaqwertyuiop" # Till K
print(b[1:9:4])

my_string = "Python"
print(my_string[0])
print(my_string[3])
print(my_string[-1])
print(my_string[-3])

my_string1 = "JavaSpringBoot"
print(my_string1[0:3])
print(my_string1[2:5])

my_stringm = "JavaKotlin"
print(my_stringm[1:7:4])
print(my_stringm[1:8:2])

fullstack = "JavaHtmlCss"
print(fullstack[::2])
print(fullstack[::-1])
print(fullstack[3::])

nums = [1,8,7,6,2,3,4,7,9]
print(nums[::3])
print(nums[1:6:2])
print(nums[1::3])

my_list = ['apple','banana','cheery','date']
print(my_list[0])
print(my_list[1])
print(my_list[1:3])
print(my_list[:2])
print(my_list[2:])

sentence = "The quick brown fox jumps over the lazy dog"
print(sentence[10:15])

numbers = [1,2,3,4,5,6,7,8,9]
print(numbers[1::2])

numbers = [1,2,3,4,5,6,7,8,9]
numbers[1:4] = [10,20,30]
print(numbers)
numbers[4:4] = [40,50]
print(numbers)