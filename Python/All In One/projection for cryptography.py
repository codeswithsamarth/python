import base64
def Show_Menu():
    print("1.Encrypt")
    print("2.Decrypt")

def Encrypt():
    global text
    global encrypt


    text = input("Enter Your Text To Encrypt:")
    encrypt = base64.b64encode(text.encode('utf-8'))
    print(f"Encrypted Code:{encrypt}")

def decrypt():
    decrypted = base64.b64decode(encrypt.decode('utf-8'))
    print(decrypted)

def Encrypt_Decrypt():
    while True:
        Show_Menu()
        option = input("Enter Your Option:")
        if option == "1":
            Encrypt()
        elif option == "2":
            decrypt()
        else:
            print(DeprecationWarning)


Encrypt_Decrypt()
