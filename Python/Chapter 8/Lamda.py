double = lambda x: x*2
print(double(5))

cube = lambda x: x*x*x
print(cube(5))

avg = lambda a,b,c: (a+b+c)/3
print(avg(11,22,33))

add = lambda a,b: (a+b)
print(add(5,77))

f = lambda x: 'Even' if x % 2 == 0 else 'Odd'
print(f(11))

f = lambda x: "Leap Year" if (x % 4==0) and (x % 100 != 0) or (x % 400 == 0) else "Not a Leap Year"
print(f(2025))

palindrome = lambda Name: "Palindrome" if Name == Name[::-1] else "Not a Palindrome Text"
print(palindrome("MADAM"))

f = lambda x,y: x*y
print(f(5,2))

# num = int(input("Enter Your Number")
#           )
# if num > 1:
#     for i in range(2,int(num ** 0.5) + 1):
#         if num % i == 0:
#             print("Not a Prime Number")
#             break
#         else:
#             print("This is a Prime Number")
#

factorial = lambda n: 1 if n == 0 else n * factorial(n-1)
print(factorial(6))

nums = [1,2,3,4,5]
squares = {x: (lambda x: x**2) (x) for x in nums}
print(squares)
# ------------------------------------------------------------------------------------------------------------

double = lambda x: x*2
print(double(21))

cube = lambda x: x**3
print(cube(21))

avg = lambda a,b,c: (a+b+c)/3
print(avg(11,22,11))

add = lambda a,b: (a+b)
print(add(5,79))

f = lambda x: "Even" if x % 2 == 0 else "Odd"
print(f(21))

leap_year = lambda x: "Leap year" if (x % 4 == 0) and (x % 100 != 0) or (x % 400 == 0) else "Not a Leap Year"
print(leap_year(2028))

palindrome = lambda x: "Palindrome Text" if x == x[::-1] else "Not a Palindrome Text"
print(palindrome("MADAM"))

Square = lambda x: x**2
print(Square(8))

uppercase = lambda x: x.upper()
print(uppercase("samarth"))

concat = lambda s1,s2,: print(s1+" "+s2)
print(concat("Samarth","Harshit"))

positive = lambda x: "Positive" if x > 0 else "Negative"
print(positive(-5))

string = lambda x: len(x)
print(string("Samarth"))

