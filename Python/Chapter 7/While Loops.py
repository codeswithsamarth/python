i = 0
while i < 5:
    print(i)
    i += 1

i = 1
while i <= 10:
    print(i)
    i += 1

i = 2
while i <= 100:
    print(i)
    i += 2

i = 1
while i <= 100:
    print(i)
    i += 2

i = 1
sum = 0
while i <= 10:
    sum = sum + i
    i = i + 1
    print(sum)

i = 1
sum = 0
while i <= 50:
    sum = sum + i
    i = i + 1
    print(sum)

i = 1
product = 1
while i < 10:
    product *= i
    i += 1
    print(product)

i = 0
while i <= 10:
    print("Hello")
    i += 1

numbers = [1,2,3,4,5,6]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1


# while True:
#     email = input("Enter Email Id:")
#     print("Valid Email Format")
#     if '@' and 'gmail.com' in email:
#         break
#     else:
#         print("Invalid Email Format Retry")

num = 2
while num < 10:
    print(num)
    num += 2

num = 0
while num < 10:
    if num % 2 == 0:
        print(num)
    num += 1

while True:
    print("This will Print Once Only")
    break

items = ['apple','banana','cheery']
index = 0
while index < len(items):
    print(items[index])
    index += 1

num = 3
while num <=30:
    print(num)
    num += 3

number = 2211
power = 3
result = 1
while power > 0:
    result *= number
    power -= 1
    print(result)

# while True:
#     operation = input("Enter Operator (+,-,*,/) or 'exit' to quit:")
#     if operation == 'exit':
#         break
#     num1 = int(input("Enter Number 1 :"))
#     num2 = int(input("Enter Number 2 :"))
#     if operation == '+':
#         print(num1 + num2)
#     elif operation == '-':
#         print(num1 - num2)
#     elif operation == '*':
#         print(num1 * num2)
#     elif operation == '/':
#         if num2 != 0:
#             print(num1 / num2)
#         else:
#             print("Cannot Divide By Zero")
#     else:
#         print("Invalid Operation ")
#

i = 1
sum = 0
while i <= 50:
    if i % 2 == 0:
        sum = sum + i
    i = i + 1
    print(sum)

