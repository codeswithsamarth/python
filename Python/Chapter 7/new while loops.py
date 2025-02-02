i = 1
while i <= 20:
    print(i)
    i += 1

i = 1
total = 0
while i <= 10:
    total += i
    i += 1

# num = int(input("Enter The Number:"))
# while True:
#     if num >=0:
#         print(f"The Number {num} is positive")
#         break
#     else:
#         print(f"The {num} is Negative")

num = 10
while num >= 1:
    print(num)
    num-=1

i = 2
while i <= 20:
    if i % 2 == 0:
        print(i)
        i += 2

# num = int(input("Enter The Number:"))
# total = 0
# while num > 0:
#     total += num % 10
#     num //= 10
#     print(total)

# num = int(input("Enter The Number:"))
# original_num = str(num)
# reversed_num = original_num[::-1]
# if original_num == reversed_num:
#     print("The Number is Palindrome")
# else:
#     print("The Number is Not Palindrome")


# num = int(input("Enter The Number:"))
# factorial = 1
# while num > 1:
#     factorial *= num
#     num -= 1
#     print(factorial)


# num1 = int(input("Enter Number 1:"))
# num2 = int(input("Enter Number 2:"))
# num3 = int(input("Enter Number 3:"))
# while True:
#     if num1>=num2 and num1>=num3:
#         print("Number 1 is Greater")
#         break
#     elif num2>=num1 and num2>=num3:
#         print("Number 2 is Greater"
#               )
#         break
#     elif num3>=num1 and num3>=num2:
#         print("Number 3 is Greater")
#         break

num = int(input("Enter The Number:"))
i = 2
while i * i <= num:
    if num % i == 0:
        print("The Number is Not a Prime Number")
        i+=1
        break
    else:
        print("The Number is a Prime Number")
        break