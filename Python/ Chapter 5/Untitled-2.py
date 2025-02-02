fruits = ["apple","bannana","orange"]
for fruit in fruits:
    print(fruit)

for i,frui in enumerate(fruit):
    print(f"{i},{frui}")

fruits = ["apple","bannana","orange"]
for fruit in reversed(fruits):
    print(fruit)


nums = [1,2,3,4,5]
for num in nums:
    if num % 2 == 0:
        print("The number is even",num)


number = [1,2,3,4,5]
char = ['a','b','c','d','e']
for num in number:
    for character in char:
        print(num,character)


numbers = [1,2,3,4,5]
for i in range(6,11):
    numbers.append(i)
    print(numbers)

name = ["samarth","sanket","harshit"]
for name_list in name:
    name.copy
    print(name_list)

name = ["samarth","sanket","harshit"]
for names in ["Srujan","rohan"]:
    name.extend(names)
    print(names)

name = ["samarth","sanket","harshit"]
for i,namex in enumerate("Sakshi"):
    name.insert(i+1,namex)
    print(name)

    fruits_remove = ['apple', 'cheery', 'date', 'banana']
    for fruits in fruits_remove[1:]:
        fruits_remove.remove(fruits)
        print(fruits_remove)


fruitf = ['apple', 'cheery', 'date', 'banana']
for i in range(3):
    fruitf.pop()
    print(fruitf)

for num in [n**2 for n in range(100) if n % 2 == 0]:
    print("This num is even",num)


nums = [1,2,3,4,5]
for num in nums[1:]:
    print(num)   

nums = [1,2,3,4,5,6,7,8]
total = 0
for num in nums:
    total += num
    print(total)