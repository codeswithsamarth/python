name = "Harry"
print(len(name))
print(name.endswith("rry"))
print(name.startswith("Ha"))
print(name.capitalize())

#String Formatting Methods
#using.format Methods
# name = "Samarth"
# age = 27
# introduction = "My name is {} and I am {} years old.".format(name,age)
# print(introduction)
# #
# name1 = input("Enter Your Name :")
# age1 = input("Enter Your Age")
# Confirmation = "Your name is {} and You are {} years old.".format(name1,age1)
# print(Confirmation)

#same as .format but uses dictionary
#format_map
person = {"names": "Samarth","Ages": 23}
promot = "My name is {names} and my age is {Ages}".format_map(person)
print(promot)

#Case Conversion Methods
namer = "Harshit"
print(namer.upper())
print(namer.lower())
print(namer.capitalize()) #capital to first letter
print(namer.title())


# Capitalize vs title = Title Make Each First word of Paragraph where capitalize to only first word


#string Information methods #returns true or false
names = "Sanket"
print(names.startswith("Sa"))
print(names.endswith("et"))
naam = "ABC"
print(naam.isalnum())
print(naam.isalpha())
DIGITS = "12A23"
print(DIGITS.isdigit())
blank = "   "
print(blank.isspace())
swq = "Hello Modi Team"
print(swq.isascii())

# username = input("Enter Your Username"
#                  )
# if username.isalpha():
#     print("Welcome{}" .format(username))
# else:
#     print("Name Error")

# strings modification Method
string = "  Hello  World  "
print(string.strip())
print(string.lstrip())
print(string.rstrip())

# Strings search and replace method
string1 = "Sam World"
print(string1.find("s"))
print(string1.rfind("a"))
print(string1.replace("World","Universe"))
print(string1.count("S"))

# string Join And Split Method
words = ["Hello", "World"]
print(" ".join(words))

# Firstname = input("Enter your First Name")
# LastName = input("Enter Your last Name")
# print(".".join([Firstname,LastName]))
#
# word = "Hello World"
# print(word.split())
# nami = input("Enter Your Name")
# age = input("Enter Your Age")
# print(age,nami.split())

# String Encoding Methods And Decoding Methods


# Miscellaneous
# Spilitness is a function which spilits the words
s = "Hello World"
print(s.splitlines())
# Partition is a function which seprate words and returns the tuple with three element


# Center Returns a centered string of length width
s5 = "Hello"
print(s5.center(10,"\t"))

# Zfill joins a 0  towards left of integers
s15 = "150"
print(s15.zfill(13))

# Rarely Used methods In Python
# ljust methods used for join or padding after character
sq = "Hello" # Ljust Pads At Right
print(sq.ljust(10, "\n"))

sq = "Hello"
print(sq.rjust(10, "*")) # Rjust Pads At Left



sw = "Hello World Lets Code With Sam"
print(sw.partition("Lets Code With Sam"))

# Case Fold Return Casefold of insensetive comparisons
sd = "HElLO"
print(sd.casefold())

swq = "Hello Modi Team"
print(swq.isascii())

decimals = "22222"
print(decimals.isdecimal())

identify = s = "myvariable"
print(identify.isidentifier())

islower = "Hello"
print(islower.islower())

isprintable = "Helloworld"
print(isprintable.isprintable())

istitle = "samarth Patil" #returns true if capatlize condition is true except false
print(istitle.istitle())

isupper = "SANKET" #RETURNS RUE IF ALL CHAR IS IN UPPERCASE CONDITION
print(isupper.isupper())

#Maketrans is also used for making Secret Code
# In Depth : returns a translation table suitable for passing a translate
table = str.maketrans('abc','123')
F1 = "abc"
print(F1.translate(table))

table2 = str.maketrans('Sanket','121212')
F2 = "Sanket"
print(F2.translate(table2))

# Remove Prefix
qw = "Hello World"
print(qw.removeprefix("Hello "))
# Remove Suffix
qwe = "Srujan Sanket"
print(qwe.removesuffix("Sanket"))

#rjust
sw = "Hello"
print(sw.rindex('H'))

#Rpartition
sqe = "Python Is Easy"
print(sqe.partition('Is'))

#Swap Case
ios = "Iphone"
print(ios.swapcase())

#Hash
username = input("Enter Your Name")
password = input("Enter Your Password")
if password.isalnum():
    print(password.__hash__())
elif password.isdigit():
    print(password.__hash__())
else:
    print("Invalid Password Conditions")


