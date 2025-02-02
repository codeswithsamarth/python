for i in range(10):
    print(i)
    i += 1

my_list = [1,2,3,4]
for item in my_list:
    print(item)

for char in "Hello":
    print(char)

my_dict = {'a':1,'b':2}
for keys in my_dict:
    my_dict.keys()
    print(keys)

fruits = ['apple','banana','orange']
for fruit in fruits:
    print(fruit)

for i,frui in enumerate(fruits):
    print(f"{i} {frui}")

nums = [7,9,82,91,88,12,4,3]
# for num in sorted(nums):
#     print(num
#           )

for num in reversed(nums):
    print(num)

for num in range(100):
    if num % 2 == 0:
        print(num,"This Number is even"
              )

numer = [1,2,3]
letters = ['a','b','c']
for num in numer:
    for lets in letters:
        print(num,lets)

# numbers = [1,2,3,4]
# for i in range(5,100):
#     numbers.append(i)
#     print(numbers)

numbers = [1,2,3,4,5]
for new_list in numbers:
    numbers.copy()
    print(new_list)

original_list = [1,2,3,4,5]
new_element = [6,7,8,9,10]
for element in new_element:
    original_list.append(element)
    print(original_list)

original_list = [1,2,3,4]
for num in [range(5,10)]:
    original_list.extend(num)
print(original_list)

fruits_lovers = ['apple','banana']
for i, fruit_l in enumerate(['cheery','strawberry']):
    fruits_lovers.insert(i+1,fruit_l)
    print(fruits_lovers)

fruits_remove = ['apple', 'cheery', 'date', 'banana']
for fruit in fruits_remove[0:2]:
    fruits_remove.remove(fruit)
    print(fruits_remove)

fruitf = ['apple', 'cheery', 'date', 'banana']
for i in range(1):
    fruitf.pop()
    print(fruitf)

numberses = range(10)
for num in [n**2 for n in numberses]:
    print(num)

even_numbers = range(101)
for evens in [n for n in even_numbers if n % 2 == 0]:
    print(evens,"This Is Even Number")

# num = int(input("Enter Number"))
# if num > 1:
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")


fruits = ['apple','banana','orange']
for l in range(len(fruits)):
    print(fruits[l])

marks = [99,77,82,93,91]
for high in marks:
    if high > 90:
        print("Highest Marks",high)

fruits = ['apple','banana','orange']
for fruit in fruits[1:3]:
    print(fruit)


nums = (1,2,3,4,5)
for num in nums:
    print(num)

nums = [1,2,3,4,5]
total = 0
for num in nums:
    total = total+num
    print(total)

nums = [1,2,3,4,5]
print(sum(nums))

numbers = [4,2,9,17,2,5]
print(max(numbers))
print(min(numbers))
# max_number = numbers[0]
# for num in numbers:
#     if num > max_number:
#         max_number = num
#         print(max_number)


#
numbers = [22,16,4,2,9,12,77]
print(max(numbers),min(numbers))

# min_numbers = numbers[0]
# for num in nums:
#     if num < min_numbers:
#         min_numbers = num
#         print(min_numbers)

numbers = [1,2,3,4,5]
reversed_list = []
for num in numbers:
    reversed_list.insert(0,num)
    print(reversed_list)

numbers = [5,4,3,2,1]
sorted_list = []
for num in numbers:
    sorted_list.insert(0,num)
    print(sorted_list)

numbers = [1,2,3,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,6,6,6]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
        print(unique_numbers)

numbers = [1,2,3,4,5
           ]
count = {}
for num in numbers:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
        print(count)

numbers = ['apple','banana','orange','apple','apple']
count = {}
for num in numbers:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
        print(count)

numbers = [1,2,3,4,5]
sum_even = 0
for num in numbers:
    if num % 2 == 0:
        sum_even += num
        print(sum_even)

fruits = (('apple','red'),('banana','yellow'),('cheery','pink'))
for fruit, colour in fruits:
    print(f"{fruit} is {colour}")

# fruits = ('apple','banana')
# more_fruits = ('cheery','date')
# for fruit in fruits + more_fruits:
#     print(fruit,end=' ')

fruits = ('apple','banana')
for repetation in fruits * 2:
    print(repetation)


fruits = ('apple','banana','cheery','apple','banana','cheery')
for counts in fruits:
    print(counts,fruits.count(counts))

numbers = (1,2,3,4,5)
print(any(x>3 for x in numbers))
print(all(x>0 for x in numbers))

# numbers = (x**2 for x in range(100))
# for num in numbers:
#     print(num)

numbers = range(100)
for num in [x**2 for x in numbers]:
    print(num)