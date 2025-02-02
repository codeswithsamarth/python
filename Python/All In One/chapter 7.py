from math import factorial

fruits = ['apple','banana','orange']
for fruit in fruits:
    print(fruit)
print("---------------------")
for i,frui in enumerate(fruits):
    print(f"{i}:{frui}")

for fruit in reversed(fruits):
    print(fruit)

nums = [1,2,3,4,5]
for num in nums:
    if num % 2 == 0:
        print("The num is even",num)

for num in range(6,11):
    nums.append(num)
    print(num)

for new in nums:
    nums.copy()
    print(new)

original_list = [1,2,3]
new_elements = [4,5,6]
for element in new_elements:
    original_list.append(element)
    print(original_list)

fruits = ['apple','banana']
for fruit in ['cheery',"date"]:
    fruits.extend(fruit)
    print(fruits)

fruit_lovers = ['apple','banana']
for i, fruit_l in enumerate(['cheery','date']):
    fruit_lovers.insert(i+1,fruit_l)
    print(fruit_lovers)

nums = int(input("Enter Your Number"))
factorial = 1
for i in range(1,nums+1):
    factorial *= i
    print(factorial)


