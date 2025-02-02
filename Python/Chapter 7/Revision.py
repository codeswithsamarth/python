fruits = ['apple','banana','cherry']
for fruit in fruits:
    print(fruit)

fruits = ['apple','banana','cherry']
for i, frui in enumerate(fruits):
    print(f"{i},{frui}")

fruits = ['apple','banana','cherry']
for fruit in reversed(fruits):
    print(fruit)

nums = [1,2,3,4,5]
for num in nums:
    if num %2 == 0:
        print(num,"This is a even Number")

nums = [1,2,3]
letters = ['a','b','c']
for num in nums:
    for lets in letters:
        print(num,lets)

numbers = [1,2,3]
for i in range(4,7):
    numbers.append(i)
    print(numbers)

numbers = [1,2,3,4]
for new_list in numbers:
    numbers.copy()
    print(new_list)

original_list = [1,2,3]
new_elements = [4,5,6]
for element in new_elements:
    original_list.append(element)
    print(original_list)

fruits = ['apple','banana']
for fruit in ['cheery','date']:
    fruits.extend(fruit)
    print(fruits)

fruit_lovers = ['apple','banana']
for i, fruit_l in enumerate(['cheery','date']):
    fruit_lovers.insert(i+1,fruit_l)
    print(fruit_lovers

        )

    fruits_remove = ['apple', 'cheery', 'date', 'banana']
    for fruits in fruits_remove[1:]:
        fruits_remove.remove(fruits)
        print(fruits_remove)

fruitf = ['apple', 'cheery', 'date', 'banana']
for i in range(3):
    fruitf.pop()
    print(fruitf)

numbers = range(11)
for num in [n**2 for n in numbers]:
    print(num)

    number_f = [1, 2, 3, 4, 5]
    for num in [n for n in number_f if n % 2 == 0]:
        print(num, "This is a even number")

fruits = ['apple', 'banana', 'orange']
for l in range(len(fruits)):
    print(fruits[l])

# fruits = ['apple','banana','orange']
# for fruit in fruits[1]:
#     print(fruits)
#
# fruits = ['apple','banana','orange']
# for fruit in fruits[1:4:2]:
#     print(fruits)


nums = [1,2,3,4,5]
for num in nums:
    print(num)

nums = [1,2,3,4,5]
total = 0
for num in nums:
    total += num
    print(total)

numb = [1,2,3,4,5]
evens = [num for num in nums if num % 2 == 0]
print(evens)

numbers = [4,2,9,1,5]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
        print(max_num)

numbers = [4,2,9,1,5]
min_num = numbers[0]
for num in numbers:
    if num<min_num:
        min_num = num
        print(min_num)

numbers =[1,2,3,4,5,5,5,5,5]
unique_num = []
for num in numbers:
    if num not in unique_num:
        unique_num.append(num)
        print(unique_num)

numbers = [1,2,3,4,5]
reversed_list = []
for num in numbers:
    reversed_list.insert(0,num)
    print(reversed_list)

    number = [1,1,2,2,2,2,3,3,3,3,3,4,4,4,4,5]
    count = {}
    for num in number:
        if num in count:
            count[num]+=1
        else:
            count[num] = 1
            print(count)

numbers = [1, 2, 3, 4, 5]
total = 0
count = 0
for num in numbers:
    total += num
    count += 1
    average = total / count
    print(average)

numbers = [1,2,3,4,5]
sum_even = 0
for num in numbers:
    if num % 2 == 0:
        sum_even += num
        print(sum_even)

        numbers = [1, 2, 3, 4, 5]
        sum_odd = 0
        for num in numbers:
            if num % 2 != 0:
                sum_odd += num
                print(sum_odd)

# Re Revision
fruits = ['apple','banana','cherry']
for fruit in fruits:
    print(fruit)

fruits = ['apple','banana','cherry','dates','Custard Apple']
for i, fruit in enumerate(fruits):
    print(f"{i},{fruit}")

fruits = fruits[:len(fruits)]
for fruit in reversed(fruits):
    print(fruit)

nums = range(10)
for num in nums:
    if num % 2 == 0:
        print(num,'These are even Number')

numbers = [1,2,3,4]
for i in range(5,11):
    numbers.append(i)
    print(numbers)

numbers = [1,2,3,4]
for new_list in numbers:
    numbers.copy()
    print(new_list)

original_list = [1,2,3,4]
new_lists = [5,6,7,8]
for concat in new_lists:
    original_list.append(concat)
    print(original_list)

fruits = ['apple','banana','cherry']
for extend in ["Strawberry Mango"]:
    fruits.extend(extend)
    print(fruits)

fruit_lovers = ['apple','banana']
for i, inserts in enumerate(["dates",'Custard Apple']):
    fruit_lovers.insert(0,inserts)
    print(fruit_lovers)

    fruits_remove = ['apple', 'cheery', 'date', 'banana']
    for fruits in fruits_remove[1:]:
        fruits_remove.remove(fruits)
        print(fruits_remove)

fruits_pop = ['apple','banana']
for pop in fruits_pop:
    fruits_pop.pop(-1)
    print(fruits_pop)

numbers = range(10)
for squares in[x**2 for x in numbers]:
    print(squares)

numb = [1,2,3,4,5]
evens = [num for num in numb if num % 2 == 0]
print(evens)

fruits = ['apple','banana','cherry']
for i in range(len(fruits)):
    print(fruits[i])

nums = [1,2,3,4,5]
total = 0
for num in nums:
    total += num
    print(total)

numbers = [4,2,98,1,5]
max_numbers = numbers[0]
for num in numbers:
    if num >= max_numbers:
        max_numbers = num
        print(max_numbers,"This is A Maximum Number")

numbers = [4,2,98,1,5]
min_number = numbers[0]
for num in nums:
    if num <= min_number:
        min_number = num
        print(min_number,"This Is A Minimum Number")

numbers = [1,2,2,2,2,3,3,3,3,3,4,4,4,5,5,5,6]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
        print(unique_numbers)

# numbers = [1,2,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5]
# total = 0
# count = 0
# for num in numbers:
#     if num in count:
#         count[num] += 1
#     else:
#         count[num] = 1
#         print(count)

numbers = [1,2,3,4,5,6,7,8,9,10]
sum_evens = 0
for num in numbers:
    if num % 2 == 0:
        sum_evens += num
        print(sum_evens)

numbers = [1,2,3,4,5,6,7,8,9,10]
sum_odd = 0
for num in numbers:
    if num % 2 !=0:
        sum_odd += num
        print(sum_odd)

numbers = [1,2,3,4,5,6,7,8,9,10]
reversed_lists = []
for num in numbers:
    reversed_lists.insert(0,num)
    print(reversed_lists)

