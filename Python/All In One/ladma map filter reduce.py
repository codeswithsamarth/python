
double = lambda x: x**2
print(double(5))

cube = lambda y: y**3
print(f"The cube of 5 is {cube(5)}")

avg = lambda x,y,z: (x+y+z)/3

add = lambda x,y: x+y

even = lambda x: "even" if x % 2 == 0 else "odd"
# print(even(int(input("Enter Number\n"))))

leap = lambda x: "leap" if (x % 4 == 0) and (x % 100 !=0) or (x % 400 == 0) else "no leap year"
print(leap(2024))

palindrome = lambda x: "palindrome" if x == x[::-1] else "No"
print(palindrome("eye"))

factorial = lambda x: 1 if x == 0 or x == 1 else x * factorial(x-1)
print(factorial(5))

uppercase = lambda x: "upper" if x.upper() else "lower"
print(uppercase("SAMARTH"))

lens = lambda x: len(x)
print(lens("SAMARTH"))


# _________________________________________________________________________________________________________________

nums = [1,2,3,4,5,6,7,8,9,10]
evens = list(filter(lambda x: x % 2 == 0,nums))
print(evens)

double = [2,4,6,8,20,40]
change = list(map(lambda x: x * x,double))
print(change)

l = [2,7,11,22,99,111]
num_to_str = list(map(lambda x: str(x),l))
print(num_to_str)

char = ["rohit","amar","amit","shubh"]
uppers = list(map(lambda x: x.upper(),char))
print(uppers)

nums = [11,22,33,44,55,66]
floats = list(map(lambda x: float(x),nums))
print(floats)

fruit = ["Apple","Banana","Orange"]
concentate = list(map(lambda x: x + " " + "Fruit",fruit))
print(*concentate

      )


l1 = [1,2,3]
l2 = [4,5,6]
add = list(map(lambda x,y: x+y,l1,l2))
print(add)


# ----------------------------------------------------------------------------------------------

nums = [1,-1,-11,-99,99,88,-00,-991]
positive = list(filter(lambda x: x if x > 0 else None,nums))
print(positive)

negative = list(filter(lambda x: x if x < 0 else None,nums))
print(negative)

a = ["Samarth","Aditya","Ajit","Amar"]
start = list(filter(lambda x: x if x[0] == "A" or x[0] == 'a' else None,a))
print(start)
start2 = list(filter(lambda x: x if x.startswith('A') else None,a))
print(start2)

mixed_num = [1,2.0,3.0,3,4.8,9,00,9.0]
flts = list(filter(lambda x: isinstance(x,float),mixed_num))
print(flts)

