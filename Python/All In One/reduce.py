from functools import reduce

sum = [1,2,3,4,5,6,7,8]
sum_ = (reduce(lambda x,y: x+y,sum))
print(sum_)

max = reduce(lambda x,y: x if x>y else y,sum)
print(max)

str = ['a','b','c','d']
concentate = reduce(lambda x,y: x+y,str)
print(concentate)

# number = int(input("Enter The Number:")
#              )
#
# factorial = reduce(lambda x,y: x*y,range(1,number+1))
# print(factorial)

numbers = [1,2,3,4,5,6,7,8,9,10]
evens = reduce(lambda x,y: x%2==0,numbers)


even_sum = reduce(lambda x,y: x+y if y%2 == 0 else x , numbers)

evens_count = reduce(lambda x,y: x+1 if y%2 == 0 else x,range(1,51))
print(evens_count)

sum_square = reduce(lambda x,y: x+y**2,range(20))
print(sum_square)

words = ['this','is','a','word'
         ]

concentate2 = reduce(lambda x,y: x+" "+y,words)
print(concentate2)