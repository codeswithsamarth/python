def add(*nums):
    total = 0
    for num in nums:
        total += num
        print(total)

def display_info(*args):
    for arg in args:
        print(arg,end=" ")
display_info("Dr","Agrawal","Mumbai","Eye_Specialist","Hospital 20","Junc-18-villa 2")


def print_address(**kwargs):
    for keys,value in kwargs.items():
        print(f"{keys}:{value}")

print_address(street="Mallikarjun Nagar",
              city="solapur",
              area="samarth Nagar",
              zip=413006)

def even(*evens):
    for even in evens:
        if even % 2 == 0:
            print(f"The {even} is even")

even(22,11,2,3,4,5,6,78,8,88,22)

def square(*args):
    for agr in args:
        print(f"The square of {agr} is  {agr**2}")


square(11,22,33,44,55)