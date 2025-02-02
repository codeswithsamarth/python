name = "Harry"
print(name.startswith("Har"))
print(name.endswith("rry"))
print(name.capitalize())

name = "Samarth"
age = 23
introduction = "My Name is {} and Age is {}".format(name,age)
print(introduction)

person = {"Name":"Samarth",'Ages':22}
prompt = "My Name is {Name} and My Age is {Ages}".format_map(person)
print(prompt)

#Case Conversion Methods
namer = "Harshit"
print(namer.upper())
print(namer.lower())
print(namer.capitalize())
print("capitalize vs title = title make each first word of Paragraph where capitalize to only first word".title())

# String Information Method Returns Bool
names = "Sanket"
print(names.isalnum())
print(names.startswith("San"))
print(names.endswith("et"))

print("1233".isdigit())
print(" a ".isspace())
print("🙂".isascii())

# strings modification Method
string = "  Hello World  "
print(string.rstrip())
print(string.strip())

# Strings search and replace method
string1 = "Hello World"
print(string1.find("o"))
print(string1.rfind("o")) # Start to search from right

print(string1.replace("World","Universe"))

words = ["hello","world"]
print(""+" ".join(words))

# First_name = input("Enter Your First Name:")
# Last_name = input("Enter Your Last Name:")
# a = " ".join([First_name,Last_name])
# print(a)


# Split lines split string by escape sequence char

s = "Hello\nworld\nHow\nare\nyou\nlets\ncode"
print(s.splitlines(keepends=True))

print("Hello\r".splitlines(keepends=True))


# partition always return a tuple with three parts include seperator


s15 = "150"
print(s15.zfill(10))

sq = "Hello"
print(sq.ljust(10,"r"))

table2 = str.maketrans('sanket','121212')
f2 = 'sanket'
print(f2.translate(table2))

qw = "hello world"
print(qw.removeprefix("hello"))

