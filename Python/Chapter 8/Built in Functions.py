
# Example 1: abs()
# The abs() function returns the absolute value of a number.
number = -7
print(abs(number))  # Output: 7

# Example 2: all()
# The all() function returns True if all elements in an iterable are true.
values = [True, True, False]
print(all(values))  # Output: False

# Example 3: any()
# The any() function returns True if any element in an iterable is true.
values = [False, False, True]
print(any(values))  # Output: True

# Example 4: ascii()
# The ascii() function returns a printable string representation of an object.
string = "hello"
print(ascii(string))  # Output: 'hello'

# Example 5: bin()
# The bin() function converts an integer to a binary string.
number = 5
print(bin(number))  # Output: '0b101'

# Example 6: bool()
# The bool() function converts a value to a Boolean (True or False).
value = 1
print(bool(value))  # Output: True

# Example 7: bytearray()
# The bytearray() function returns a bytearray object.
byte_values = bytearray([65, 66, 67])
print(byte_values)  # Output: bytearray(b'ABC')

# Example 8: bytes()
# The bytes() function returns a bytes object.
byte_values = bytes([65, 66, 67])
print(byte_values)  # Output: b'ABC'

# Example 9: callable()
# The callable() function checks if an object is callable (e.g., a function).
def example_function():
    pass
print(callable(example_function))  # Output: True

# Example 10: chr()
# The chr() function returns a string representing a character for a given Unicode code point.
unicode_value = 65
print(chr(unicode_value))  # Output: 'A'

# Example 11: classmethod()
# The classmethod() function converts a method into a class method.
class MyClass:
    @classmethod
    def greet(cls):
        print("Hello from the class!")
MyClass.greet()  # Output: Hello from the class!

# Example 12: compile()
# The compile() function compiles source code into a code object.
code = compile('x = 10', 'test.py', 'exec')
exec(code)
print(x)  # Output: 10

# Example 13: complex()
# The complex() function creates a complex number.
number = complex(2, 3)
print(number)  # Output: (2+3j)

# Example 14: delattr()
# The delattr() function deletes an attribute of an object.
class MyClass:
    x = 5
delattr(MyClass, 'x')
print(hasattr(MyClass, 'x'))  # Output: False

# Example 15: dict()
# The dict() function creates a dictionary from key-value pairs.
my_dict = dict(a=1, b=2)
print(my_dict)  # Output: {'a': 1, 'b': 2}

# Example 16: dir()
# The dir() function returns a list of attributes of an object.
print(dir([]))  # Output: List of attributes of list

# Example 17: divmod()
# The divmod() function returns the quotient and remainder of a division.
quotient, remainder = divmod(9, 4)
print(quotient, remainder)  # Output: 2 1

# Example 18: enumerate()
# The enumerate() function returns an enumerate object, useful for looping with index.
my_list = ['apple', 'banana', 'cherry']
for index, value in enumerate(my_list):
    print(index, value)
# Output:
# 0 apple
# 1 banana
# 2 cherry

# Example 19: eval()
# The eval() function executes a Python expression and returns the result.
x = 5
result = eval('x + 2')
print(result)  # Output: 7

# Example 20: exec()
# The exec() function executes Python code dynamically.
code = 'x = 10'
exec(code)
print(x)  # Output: 10

# Example 21: filter()
# The filter() function filters elements based on a function.
my_list = [1, 2, 3, 4, 5]
result = filter(lambda x: x > 2, my_list)
print(list(result))  # Output: [3, 4, 5]

# Example 22: float()
# The float() function converts a value to a floating point number.
value = '3.14'
print(float(value))  # Output: 3.14

# Example 23: format()
# The format() function formats a string using placeholders.
name = "Alice"
age = 30
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)  # Output: My name is Alice and I am 30 years old.

# Example 24: frozenset()
# The frozenset() function creates an immutable set.
my_frozenset = frozenset([1, 2, 3])
print(my_frozenset)  # Output: frozenset({1, 2, 3})

# Example 25: getattr()
# The getattr() function returns the value of an attribute from an object.
class MyClass:
    x = 5
print(getattr(MyClass, 'x'))  # Output: 5

# Example 26: globals()
# The globals() function returns the global namespace as a dictionary.
print(globals())  # Output: {'__name__': '__main__', 'x': 5, ...}

# Example 27: hasattr()
# The hasattr() function checks if an object has a specific attribute.
print(hasattr(MyClass, 'x'))  # Output: True

# Example 28: hash()
# The hash() function returns the hash value of an object.
print(hash('hello'))  # Output: hash value

# Example 29: help()
# The help() function displays the help information for an object.
help(str)  # Displays help for the 'str' class

# Example 30: hex()
# The hex() function converts an integer to a hexadecimal string.
print(hex(255))  # Output: '0xff'

# Example 31: id()
# The id() function returns the unique identifier of an object.
print(id('hello'))  # Output: unique ID value

# Example 32: input()
# The input() function reads user input from the command line.
name = input("Enter your name: ")  # User input
print("Hello,", name)

# Example 33: int()
# The int() function converts a value to an integer.
value = '42'
print(int(value))  # Output: 42

# Example 34: isinstance()
# The isinstance() function checks if an object is an instance of a class.
print(isinstance(5, int))  # Output: True

# Example 35: issubclass()
# The issubclass() function checks if a class is a subclass of another.
class A: pass
class B(A): pass
print(issubclass(B, A))  # Output: True

# Example 36: iter()
# The iter() function returns an iterator object for an iterable.
it = iter([1, 2, 3])
print(next(it))  # Output: 1

# Example 37: len()
# The len() function returns the length of an object.
print(len('hello'))  # Output: 5

# Example 38: list()
# The list() function converts an iterable to a list.
print(list((1, 2, 3)))  # Output: [1, 2, 3]

# Example 39: locals()
# The locals() function returns the local namespace as a dictionary.
def func():
    x = 5
    print(locals())  # Output: {'x': 5}
func()

# Example 40: map()
# The map() function applies a function to each item in an iterable.
print(list(map(lambda x: x**2, [1, 2, 3])))  # Output: [1, 4, 9]

# Example 41: max()
# The max() function returns the largest item from an iterable.
print(max([1, 2, 3]))  # Output: 3

# Example 42: memoryview()
# The memoryview() function creates a memory view object.
mv = memoryview(b'abc')
print(mv[0])  # Output: 97 (ASCII value of 'a')

# Example 43: min()
# The min() function returns the smallest item from an iterable.
print(min([1, 2, 3]))  # Output: 1

# Example 44: next()
# The next() function retrieves the next item from an iterator.
it = iter([1, 2, 3])
print(next(it))  # Output: 1
