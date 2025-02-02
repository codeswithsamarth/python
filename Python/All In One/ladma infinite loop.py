# lambda function is unknown function
from math import factorial

square = lambda x: x**2
print(square(10))

cube = lambda x: x**3
print(cube(24))

avg = lambda x,y,z: (x+y+z)/3
print(avg(11,22,33))

evens = lambda x: "Even" if x % 2 == 0 else "odd"
print(evens(16
            ))

# leap = lambda year: "leap" if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else "Not a leap year"
# print(leap(int(input("Enter Year To check:"))))
#
# palindrome = lambda text: "Palindrome" if text == text[::-1] else "Not a Palindrome"
# print(palindrome(input("Enter Text To check:")))
#

factorials = lambda x: 1 if x == 0 else x*factorials(x-1)
print(factorials(5))

