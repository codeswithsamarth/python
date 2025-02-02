# map() = applies a function to each item in an iterable(list,tuple,etc)

# map(function,iterable)


# def is_even(a):
# #     return a%2 ==0
# nums = [3,2,4,5,6,9,7,8]
# evens = list(filter(is_even,nums))
# print(evens)

nums = [3,2,4,5,6,9,7,8]
evens = list(filter(lambda x: x % 2 == 0,nums))
print(evens)

double = list(map(lambda x: x * 2,evens))
print(double)

from functools import reduce

sum = reduce(lambda a,b: a+b ,double)
print(sum)

def cube(x):
    return x*x*x
print(cube(2))

l = [2,3,4,5,6,7,8,9]
squares = list(map(lambda x:x**2,l))
print(squares)

sub = list(map(lambda x:x-1,squares))
print(sub)

l1 = [2,3,4,5,6,7,8]
result = list(map(lambda x: str(x),l1))
print(result)

l2 = ["sanket","harshit","samarth"]
result = list(map(lambda x: x.upper(),l2))
print(result)

nums = [11,22,33,44,55,66,88]
squares = list(map(lambda x: x**2,nums))
print(squares)

strings = ["Samarth","Sanket"
           ]
# result = list(map(lambda x: x +'!' ,strings))
# print(result)
#
reve = list(map(lambda x: x[::-1],strings))
print(reve)

first_last = list(map(lambda x: x[0]+x[-1],strings))
print("Hi",*first_last)

numbers = [1,2,3,4,5,6,7,8,9,10]
evens = list(filter(lambda x: x % 2 == 0,numbers))
print(evens)

odd = list(filter(lambda x: x%2 !=0,numbers))
print(odd)

nums = [1,-1,-11,-99,99,88,-00,-991]
positive = list(filter(lambda x: x if x > 0 else None,nums))
print(positive)

negative = list(filter(lambda x: x if x < 0 else None,nums))
print(negative)

strings = ["a","","c"]
non_empty = list(filter(lambda x: x if x != "" else None,strings))
print(non_empty)

nums = [1,2,3,4,5,6,7,8]
greater = list(filter(lambda x: x if x > 3 else None,nums))
print(greater)

less = list(filter(lambda x: x if x < 3 else None,nums))
print(less)

string = ["Samarth","Anand","Aakash","Arvind"]
a = list(filter(lambda x:x if x[0] == "A" or x[0] == 'a' else None,string))
print(a)

a = [3,2,6,4,9,6,12,8,15,10]
divisible_by_3 = list(filter(lambda x: x if x % 3 == 0 else None,a))
print(divisible_by_3)

palindromes = ["Ravi","CIVIC","MADAM","RACECAR","Samarth"]
is_palindromes = list(filter(lambda x: x if x == x[::-1] else None,palindromes))
print(is_palindromes)

lower = ["samarth","Sanket","Samarth",'sanket']
is_lower = list(filter(lambda x: x if 'x'.islower() else None,lower))
print(is_lower)

mixed_numbers = [1,2,0.5,9.0,2.5,7.32,8.84,0.213,92.92]
lower = list(filter(lambda x: isinstance(x,float),mixed_numbers))
print(lower)

mixed_str = ["samarth",22,"sanket",42,"harshit","69"]
strs = list(filter(lambda x: isinstance(x,str),mixed_str))
print(strs)