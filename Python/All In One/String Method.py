my_city = "New York"
print(type(my_city))

word1 = "New"
word2 = "York"
print(word1 +" "+ word2)
print(len('rio'))

State = "Rio de Janeiro"
print(State.replace("Rio","Mar"))

name = "Sasas"
print(name.count("s"))

words = "Tokyo" * 3
print(words)

my_phrase = "Let\'s Go To The Beach"
my_phrases = my_phrase.split(" ")
print(my_phrases)

my_csv = "mary;32;austrilla;marry@gmail.com"
my_csvs = my_csv.split(';')
print(my_csvs[3])

# name = input("Enter Your Name")
# age = input("Enter Your Age")
# # introduction = "My Name is {} and My age is {}".format(name,age)
# # print(introduction)
#
# person = {"name":name,"age":age}
# promt = "My name is {name} and my age is {age}".format_map(person)
# print(promt)

# Case Conversion Method
namer = "harshit andewadi"
print(namer.lower())
print(namer.upper())
print(namer.capitalize())
print(namer.title())

# Capitalize vs title = Title Make Each First word of Paragraph where capitalize to only first word

# String Information Methods
names = "Sanket"
print(names.startswith("sa"))
print(names.endswith("et")
      )
naam = "ABC@"
print(naam.isalpha())
print(naam.isalnum())

digits ="12345"
print(digits.isdigit())

space = " m "
print(space.isspace())

# strings modification Method
string = "  Hello World  "
print(string.strip())
print(string.lstrip())
print(string.rstrip())

# Strings search and replace method
string1 = "Sam World"
print(string1.find("S"))
print(string1.rfind("a"))
print(string1.replace("World","Universe"))
print(string1.count("S"))

info = "Samarth,32,9731454964,Samarthp2727@gmail.com"
split_manager = info.split(",")
print(split_manager)
print(split_manager[2:])

# Splitlines is a method which spilt String Based on Split character
text = "Hello\nworld\nwelcome\nto\nPython"
print(text.splitlines())

s5 = "Hello"
print(s5.center(10,"\n"))

s15 = ("Hello")
print(s15.zfill(13))

sq = "Hello"
print(sq.rjust(10,"@"))

a = sq.ljust(10,";")
print(a)

sd = "HelLo"
print(sd.casefold())

decimal = "2222"
print(decimal.isdigit())

print("Samarth".isidentifier())

lower = "hello"
print(lower.islower())

isprintable = "Hello\nworld"
print(isprintable.isprintable())


s = "Hello, what\'s up"
print(s)

print("Multiple strings\ncan be created\nusing escapesequence")

