# map applies function to each item of an iterable
# map = (function,iterable)

nums = [1,2,3,4,5,6,7,8,9,10]
evens = list(filter(lambda x: x % 2 == 0,nums))
print(evens)

double = list(map(lambda x: x*2,evens))
print(double)

l = [3,2,4,5,6,8,10,29]
square = list(map(lambda x: x*x,l))
print(square)

l = [2,7,11,22,99,111]
num_to_str = list(map(lambda x: str(x),l))
print(num_to_str)

char = ["rohit","amar","amit","shubh"]
upper = list(map(lambda x: x.upper(),char))
print(upper)

reverse = list(map(lambda x: x[::-1],char))
print(reverse)

first = ["Samarth"]
first_last = list(map(lambda x: x[0] + x[1],first))
print(first_last)

nums = [11,22,33,44,55,66]
flt = list(map(lambda y: float(y),nums))
print(flt)

each_five = list(map(lambda x: x+5,nums))
print(each_five)

strings = ["samarth","apparao","pati","shubh","sankey"]
uppers = list(map(lambda x: x.upper() , strings))
print(uppers)

capitalize = list(map(lambda x: x.capitalize(),strings))
print(capitalize)

double = [11,22,33,44,55,66]
doubled = list(map(lambda x: x*2,double))
print(doubled)

flts = [1.1,2.2,3.3,4.6]
inties = list(map(lambda x: int(x) ,flts))
print(inties)

numbers = [1,2,3,4,5,6,7,8]
sub_two = list(map(lambda x: x-2,numbers))
print(sub_two)

fruit = ["Apple","Banana","Orange"]
concent_fruit = list(map(lambda x: x+" "+"Fruit",fruit))
print(*concent_fruit)

numbers = [1,2,3,5,7,9,10,92,13]
multiply_by_ten = list(map(lambda x: x*10,numbers))
print(multiply_by_ten)

lengths = ["Samarth","Aakash"]
lengthi = list(map(lambda x: len(x),lengths))
print(lengthi)

l1 = [1,2,3]
l2 = [4,5,6]
add = list(map(lambda x,y: x+y,l1,l2))
print(add)

multiply = list(map(lambda x,y: x*y,l1,l2))
print(multiply)

d1 = [10,20,30]
d2 = [5,10,10]
divide = list(map(lambda x,y: x/y,d1,d2))
print(divide)

bools = [True,False,True,False]
bool_to_str = list(map(lambda x: str(x),bools))
print(bool_to_str)


numbers = [1,2,3,4,5,6,7,8,9,10]
evens = list(filter(lambda x: x % 2 == 0,numbers))
print(evens)
odd = list(filter(lambda x: x % 2 != 0,numbers))
print(odd)

nums = [1,-1,-11,-99,99,88,-00,-991]
positive = list(filter(lambda x: x if x > 0 else None,nums))
print(positive)

negative = list(filter(lambda x: x if x<0 else None,nums))
print(negative)

strings = ["a","","c"]
non_empty = list(filter(lambda x: x if x != "" or x.isspace else None,strings))
print(non_empty)

nums = [1,2,3,4,5,6,7,8]
greater = list(filter(lambda x: x if x > 3 else None,nums))
print(greater)
lower = list(filter(lambda x: x if x < 5 else None,nums))
print(lower)

a = ["Samarth","Aditya","Ajit","Amar"]
start = list(filter(lambda x: x if x[0] == "A" or x[0] == 'a' else None,a))
print(start)
start2 = list(filter(lambda x: x if x.startswith('A') else None,a))
print(start2)

a = [2,3,4,6,6,9,8,12,10,15]
divisible_by_3 = list(filter(lambda x: x if x % 3 == 0 else None,a))
print(divisible_by_3)

palindrome = ["Ravi","CIVIC","MADAM","RACECAR","Samarth"]
is_palindrome = list(filter(lambda x: x if x == x[::-1] else None,palindrome))
print(is_palindrome)

mixed_num = [1,2.0,3.0,3,4.8,9,00,9.0]
flts = list(filter(lambda x: isinstance(x,float),mixed_num))
print(flts)

lists = [1,2,3,4,5,6,7,8,9]
add_two = list(map(lambda x: x+2,lists))
print(add_two)

square_to_each = list(map(lambda x: x**2,lists))
print(square_to_each)

list_str = ["SAMARTH","PATIL","LEARNS","PYTHON"
            ]
lower_to_all = list(map(lambda x: x.lower(),list_str))
print(*lower_to_all)

each_three = list(map(lambda x: x*3, lists ))
print(each_three)

strs = ["1","2","3"]
str_to_int = list(map(lambda x: int(x),strs))
print(str_to_int)

str_to_ = ["Samarth","Patil"]
exclamation_to_str = list(map(lambda x: x+'!',str_to_))
print(exclamation_to_str)

count_word = list(map(lambda x: len(x),str_to_))
print(count_word)

lisrt = [11,22,33,44,55]
doubled_doubled = list(map(lambda x: x*2,lisrt))
print(doubled_doubled)

numbers = [1,2,3,4,5]
evens = list(map(lambda x: x if x % 2 == 0 else None,numbers))
print(evens)

empty_str = ["S","","","s",""]
empty_strs = list(map(lambda x: x.replace("","N/A")if x == "" else x,empty_str))
print(empty_strs)

numbers = [2,-3,4,5,-6,7,-8,9]
ps = list(map(lambda x: x**2 if x > 0 else x,numbers))
print(ps)

lists = ["Sa","Fu","Hongkong",None,"Da","vinchi","Us",None]
none_replace = list(map(lambda x: "Unknown" if x == None else x,lists))

print(none_replace)

numbers = [-6,2,4,5,-3,2,6,8]
positive_negative = list(map(lambda x: f"Positive" if x > 0 else "Negative",numbers))
print(positive_negative)

words = ["Brave","Strong","Fine"]
ends_with = list(map(lambda x: x+"ly" if x.endswith("e") else x,words))
print(ends_with)

a = [3,9,2]
b = [5,7,4]
greater = list(map(lambda x,y: x if x > y else y,a,b))
print(greater)