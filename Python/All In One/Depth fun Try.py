b = "Python;is;a;powerful;language"
print(b.split(";",2))

text = 'John, Doe, "1234 Elm St, Apt 5", "New York, NY" 30'
print(text.split(",",2))

text2 = "apple banana orange grape mango"
print(text2.split(" ",2))

text3 = "2024-11-19 12:30:00 INFO Log entry"
print(text3.split(" ",2))

text4 = "one;two;three;four;five;six"
print(text4.split(";",2))

text5 = "name:John;age:30;city:New York;country:USA"
print(text5.split(";",2))

text6 = "apple,banana,orange,grape,mango"
print(text6.split(",",2))

text7 = "book-title,author,publisher,year,price"
print(text7.split(",",2))

# _--------------------------------------------------------------

# partition always return a tuple with three parts include seperator

text = "apple-orange"
result = text.partition("-")
print(result)


# --------------------------------------------------

text = "Hello World"
encoded_text = text.encode('utf-8')
print(encoded_text)

decoded_text = encoded_text.decode("utf-8")
print(decoded_text)

text = "Hello!"
encoded_text = text.encode("ascii")
print(encoded_text)

decoded_text = encoded_text.decode()
print(decoded_text)

import base64
text = "I am Track You Anywhere Anytime"
encoded_text = base64.b64encode(text.encode('utf-8'))
print(encoded_text)

decoded_text = encoded_text.decode('utf-8')
print(decoded_text)

decoded_text2 = base64.b64decode(encoded_text.decode('utf-8'))
print(decoded_text2)

# import urllib.parse
# text = "I How Are You ! Fine Dude"
# encoded_text = urllib.parse.urlencode(text)
# print(encoded_text)

from cryptography.fernet import Fernet

key = Fernet.generate_key()
key2 = Fernet(key)

text = "Hi Dude Lets Do 1v1"

encrypted_text = key2.encrypt(text.encode())
print(f"Encrypted {encrypted_text}")

decrypted_text = key2.decrypt(encrypted_text.decode())
print(f"Decode:{decrypted_text}")


import base64

text = "Samarth"
encrypt = base64.b64encode(text.encode('utf-8'))
print(encrypt)

decodes = base64.b64decode(encrypt.decode('utf-8'))
print(decodes)

import urllib.parse
text = "I How Are You ! Fine Dude"
encoded_text = urllib.parse.quote(text)
print(encoded_text)

import cryptography.fernet

key1 = Fernet.generate_key()
key2 = Fernet(key1)

# message = input("Enter Your Message:")
# encrypt = key2.encrypt(message.encode('utf-8'))
# print(encrypt)
#
# decrypt = key2.decrypt(encrypt.decode('utf-8'))
# print(decrypt)

import hashlib


def Show_Menu():
    print("1. Encode")
    print("2. Decode")

def inp():
    message = input("Enter Message: ")
    return message


def convert_Encode(message):
    # Hash the message using SHA-256 and return the hexadecimal digest
    encrypt = hashlib.sha256(message.encode()).hexdigest()
    return encrypt


def decrypt(original_hash):
    # Get the hashed message from the user to compare with the original hash
    messages = input("Enter code to Decrypt: ")
    if messages == original_hash:
        print("Valid code!")
    else:
        print("Check Code Invalid")


def Cryptograpy():
    original_hash = None

    while True:
        Show_Menu()
        option = input("Enter Option To Proceed: ")

        if option == "1":
            # Encoding option
            message = inp()  # Get the message to encode
            original_hash = convert_Encode(message)  # Get the hash
            print("Encoded Message (Hash):", original_hash)

        elif option == "2":
            # Decoding option (checking if the input matches the original hash)
            if original_hash:
                decrypt(original_hash)  # Compare input with the original hash
            else:
                print("No message encoded yet.")

        else:
            print("Invalid Option")


# Start the program
Cryptograpy()
