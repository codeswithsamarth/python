def goodDay(name,ending):
    print(f"Good Day,",name)
    print(ending)
goodDay("Samarth","Thankyou")
goodDay("Rohan","Thankyou")

def goodDay(name):
    print(f"Good Day,",name)
    return "Done"
a = goodDay("Samarth")
print(a)



def greet(name):
    print(f"Hello {name} Sir")
greet("Srujan")


def add(a,b):
    print(a+b)
add(5,3)

def say_hello(name1,name2):
    print(f"Hello {name1} and {name2}")
say_hello("Harshit","Sanket")

def multiply(a,b,c):
    print(a*b*c)
multiply(2,3,4)

def is_true(value):
    if value:
        print("It is True")
    else:
        print("It is False")
is_true(True)


def print_float(num):
    print(f"The number is {num}")
print_float(23)


def show_items(items):
    for item in items:
        print(item)
show_items([22,44,66,77 ])

def print_coordinates(coords):
    print(f"x = {coords[0]}, y = {coords [1]}")
print_coordinates((11,11))

def show_info(info):
    print(f"Name : {info['name']},Age : {info['Age']}")
show_info({"name" : "Alice ","Age" : 24})

def print_dimensions(dimension):
    length,width,height = dimension
    print(f"Length : {length}, Width {width}, Height {height}")
print_dimensions([11,22,33])

def print_values(values):
    a,b = values
    print(f"a : {a}, b : {b}")
print_values({11,22})


def get_dimensions(dimensions):
    print(f"Width : {dimensions[0]} Height : {dimensions[1]}")
get_dimensions((800,600))

def first_last_elements(lst):
    print(f"First {lst[0]} Last {lst[-1]}")
first_last_elements([11,22,33,44,55])

def city_state_country(location):
    print(f"City {location[0]} State {location[1]} Country {location[2]} ")
city_state_country(("I am Solapur","Maharastra","India"))


def get_time(time):
    print(f"Hours {time[0]} Minutes {time[1]} Seconds {time[2]}")
get_time((11,22,33))


def product_price(product):
    print(f"Product {product[0]} Price {product[1]}")
product_price(("Laptop",22))

def cars_info(car):
    print(f"Choice {car[0]} Model {car[1]} Price {car[2]}")
cars_info(("Tesla","Model X",100000))

def Grade_system(student):
    print(f"Name {student[0]} Grade {student[1]}")
Grade_system(("Samarth",22))

def account_details(account):
    print(f"Account Number {account[0]} Account Balance {account[1]}")
account_details((22265645487,65654))


def hotels_rating(hotel):
    print(f"Hotel 1 : {hotel[0]} , Rating {hotel[1]}, Hotel 2 {hotel[2]} Rating {hotel[3]} ")
hotels_rating(("A",4.5,"b",4.7))

def goodDay(name,ending):
    print(f"Good Day,",name)
    print(ending)
goodDay("Samarth","Thankyou")
goodDay("Rohan","Thankyou")

def add(a,b):
    print(a+b)

add(11,44)


def say_hello(Name1,Name2):
    print(f"Hello {Name1} and {Name2}")
say_hello("Harshit","Sanket")

def max_items(Items):
    print(max(Items))
max_items([11,22,33,44,77,99,112])


def sort(nums):
    print(sorted(nums))
sort([77,44,99,88,33,12,0,1,2,20,22])


# def email_format_checker():
#     domain1 = "@gmail.com"
#     domain2 = "@Yahoo.com"
#     domain3 = "@hotmail.com"
#     email = input("Enter Your Email")
#     a = "Email Valid Format"
#     while True:
#         if domain1 in email:
#             print(email, a)
#             break
#         elif domain2 in email:
#             print(email, a)
#             break
#         elif domain3 in email:
#             print(email, a)
#             break
#         else:
#             print("Invalid Email Format")
#             break
# email_format_checker()
#

def print_coordinate(Values):
    print(f"X = {Values[0]} Y = {Values[1]} ")
print_coordinate(["2","7"])


def user_name(Info):
    print(f"Name = {Info[0]} Age {Info[1]} City {Info[2]}")
user_name(["Samarth",22,"Solapur"])

def sum_first_last(Nums):
    first = Nums[0]
    last = Nums[-1]
    sum = first + last
    print(sum)
sum_first_last([11,22,33,4,77])

def location_state_city(Info):
    print(f"Location {Info[0]} State {Info[1]} City {Info[2]}")
location_state_city(["Solapur","Lies In State Maharashtra","In Asia Contient India"])


def multiply_and_divide(a,b):
    product = a*b
    division = a/b
    print(f"Product {product} Division {division}")
multiply_and_divide(11,22)

def power(base,power):
    power_result = base ** power
    print(power_result)
power(112,2)

def describe_pet(pet_name,Breed,animal_type):
    print(f"I have a {animal_type} His Name is {pet_name} And It\'s Breed is {Breed}")
describe_pet("Reo","Pomerion","Dog")
describe_pet("Meo","Meo","Cat")
