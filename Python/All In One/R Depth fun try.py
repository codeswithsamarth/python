b = "Python;is;a;powerful;language"
print(b.split(';',2))

text = 'John, Doe, ""1234 Elm St, Apt 5", "New York, NY" 30'
print(text.split(",",2))

text2 = "apple banana orange grape mango"
print(text2.split(" ",2))

text4 = "John;software-engineer;23;Usa;9283;lati-23-plot6"
info = text4.split(';',3)
necessary = info[:3]
print(necessary)

# text7 = "book-title,author,publisher,year,price"
# text_split = text7.split(",",2)
# text_limit = text_split[:2]
# print(text_limit)


# Split lines split string by escape sequence char

s = "Sam\n23\nUI-UX-Design\nApex-Company"
info = s.splitlines()
Necessary_S = info[:3]
print((f"Provided[{info}],Necessary[{Necessary_S}]"))

# Partition
# Brief : First as It is Second Seperator Third All Combo

text = "Hello World"
part = text.partition(' ')
print(part)

# ---------------------------------------------------

text = "Hello World"
encoded_text = text.encode('utf-8')
print(encoded_text)

decoded_text = encoded_text.decode('utf-8')
print(decoded_text)

import base64
text = "I am Tracking You"
encoded_text = base64.b64encode(text.encode('utf-8'))
print(encoded_text)

decoded_text = base64.b64decode(encoded_text.decode('utf-8'))
print(decoded_text)

# text = input("Enter Your Text To Encode:")
# encoded_text = base64.b64encode(text.encode('utf-8'))
# print(encoded_text)

import urllib.parse
text = "Baap To Baap Rahega"
encoded_text = urllib.parse.quote(text)
print(encoded_text)

from cryptography.fernet import Fernet

key = Fernet.generate_key()
key2 = Fernet(key)

text = "Hi Dude Lets Do 1v1"

encrypted_text = key2.encrypt(text.encode())
print(f"Encrypted {encrypted_text}")

decrypted_text = key2.decrypt(encrypted_text.decode())
print(f"Decode:{decrypted_text}")

import hashlib

text = input("Enter Text To Hash It:")
encrypted_text = hashlib.sha256(text.encode()).hexdigest()
print(encrypted_text)

