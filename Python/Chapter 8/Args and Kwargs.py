# *args = allows you to pass multiple non-key arguments # Packs Over Tuple
# *kwargs = allows you to pass multiple keyword arguments # Packs over Dictonary

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(add(1,2,3,4))


def display_name(*args):
    for arg in args:
        print(arg,end=" ")
display_name("Dr","Spongebob","Harold","Squarepants","III")

def print_address(**kwargs):
    for keys,value in kwargs.items():
        print(f"{keys}:{value}")
print_address(street="Mallikarjun Nagar"
              ,city="Solapur",
              state="Maharashtra",
              zip=413006)

# key point = We Can Never Pass Kwargs before Agrs in Multiple using Case
def shipping_label(*args,**kwargs):
    for value in args:
        print(value)
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")
shipping_label("Dr","Spongebob","III",
               street = "123 Fake Street",
               apt = 100,
               city = "Detroit",
               state = "MI",
               zip = "54321")

def even(*args):
    for arg in args:
        if arg % 2 == 0:
            print(arg)

even(11,22,44,88,55)

def even_sum(*args):
    sum = 0
    for arg in args:
        if arg % 2 == 0:
            sum += arg
            print(sum)

even_sum(2,4,7,8,12,14,18,22)

# def prime_number():
#     num = int(input("Enter Your Number")
#               )
#     if num > 1:
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 print("Not a Prime Number")
#                 break
#             elif num % i != 0:
#                 print("This is a Prime Number")
#
#
# prime_number()

# def leap():
#     year = int(input("Enter Year To check Leap Or Not:"))
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print("Year Is Leap Year")
#     else:
#         print("Not a Leap Year")
#
# leap()

# def triangle_type():
#     a = int(input('Enter Triangle Side 1 :'))
#     b = int(input('Enter Triangle Side 2 :'))
#     c = int(input('Enter Triangle Side 3 :'))
#     if a == b == c:
#         print("Equilateral triangle")
#     elif a == b or b == c or a == c:
#         print("Isosceles Triangle")
#     else:
#         print("Scalene Triangle")
#
# triangle_type()
#

# def palindrome():
#     text = input("Enter Your Text")
#     if text.upper() == text.upper()[::-1]:
#         print("This is a Palindrome Text")
#     else:
#         print("Not a Palindrome text")
#
# palindrome()



def add(*numbers):
    return sum(numbers)
print(add(11,22,33,44,55))


# def infos(*info):
#     for inf in info:
#         print(inf,end= " ")
# infos("Samarth","Akaak","Skdsk","Skdlsl")



def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total
add(11,22,33,44,55)

def display_name(**kwargs):
    for keys,value in kwargs.items():
        print(f"{keys} {value}")

display_name(Name = "Samarth",
             Age = 23,
             City = 23,
             Apt =100,
             State = "Mahrashtra")


def square(*args):
    for num in args:
        print(f"The Square of Number is {num} is {num ** 2} ")
square(22,44,66,77,88,11,22)

def cube(*args):
    for arg in args:
        print(f"The Cube of {arg} is {arg ** 3}")
cube(22,44,55,66,77,88,99)


def even_numbers(*nums):
    for num in nums:
        if num % 2 == 0:
            print("The num is even")
        else:
            print("The Num is odd")
even_numbers(int(input("Enter Number:")))


# def square_numbers(*args):
#     for squared in args:
#         print(f"The Square of {squared} is {squared ** 2}")
#
# square_numbers(int(input("Enter Numbers")))


# def multiple_square():
#     squares = int(input("Enter Number to Square it:"))
#     print(f"The square of {squares} is {squares ** 2}")
# multiple_square()
#
# def m():
#     multiple_square()
#     multiple_square()
#     multiple_square()
# m()
#
# def m2():
#     m()
#     m()
#     m()
#     m()
# m2()

