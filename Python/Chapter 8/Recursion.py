"""
factorial(5) = 5 X 4 X 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1
factorial(3) = 3 X 2 X 1
factorial(2) = 2 X 1
factorial(1) = 1

factorial(n) = n X n-1 X ......3X2X1
factorial(n) = n * factorial(n-1)
"""

# Recursion is a function which calls itself.
# which can be solved iteratively or recursively
"""
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X1
factorial(5) = 5 X 4 X 3 X 2 X 1

"""

# Factorial(n) = n X n-1 X .....3X2X1
# factorial(n) = n*factorial(n-1)


# def factorial(n):
#     if (n==1 or n==0):
#         return 1
#     return n * factorial(n-1)
# n = int(input("Enter a Number"))
# print(f"The factorial of this number is {factorial(n)}")
#
#
def walk(step):
    for step in range(1,step + 1):
        print(f"You take step {step}")
walk(100)

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
print(factorial(10))

# import sys
# sys.setrecursionlimit(2000)
# i = 1
# def greet():
#     global i
#     i+=1
#     print("Hello",i)
#     greet()
# greet()


# import sys
# print(sys.getrecursionlimit())
# print(sys.setrecursionlimit(200))
# def demo():
#     print("hello")
#     demo()
# demo()

# n = int(input("Enter the value of N"))
# def natural(n):
#     if n == 0:
#         return
#     print(n)
#     return natural(n-1)
# natural(n)

def even_nums(num):
    print(num)
    if num == 2:
        return num
    else:
        return even_nums(num-2)


def fib(n):
    print(0)
