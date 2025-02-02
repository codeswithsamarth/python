import time
def time_measure(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        time.sleep(0.1)
        end = time.time()
        print(func.__name__+"took",str((end-start)*1000))
        return result
    return wrapper


# Simple Mobile Banking App

# DBMS To Store User Data

_username = "Samarthp1234"
_password = "SAMA_2008"

# Function For Login

def login():
    username = input("Enter Your Username:")
    password = input("Enter Your Password:")

    if username == _username and password == _password:
        print(f"Welcome {username} Login Successful")
        return True
    else:
        print("Invalid Login Credentials")
        return False

# Function for Transfer Money

def transfer_money(balance):
    amount = float(input("Enter the Amount to Transfer"))
    user = input("Enter Users Account Number")

    if amount > balance:
        print("Insufficient Balance")
    else:
        balance -= amount
        print(f"The Fund is Transferred , New Balance is {balance}")
    return balance


def receive_money(balance):
    amount = float(input("Enter the Amount to Transfer"))
    sender = float(input("Enter Your Account Number"))
    if amount > balance:
        print("Insufficient Balance")
    else:
        balance += amount
        print(f"The Fund is Received By {sender}, New Balance is {balance}")
        return balance
def bank_balance(balance):
    print(f"Your Bank Balance is {balance}")
    return balance

def invest_in_gold(balance):
    amount = float(input("Enter Amount to Invest in Gold"))
    if amount > balance:
        print("Insufficient Balance")
    else:
        balance -= amount
        print(f"The Fund is Invested in Gold")
        return balance

def invest_in_crypto(balance):
    amount = float(input("Enter Amount to Invest in Crypto"))
    if amount > balance:
        print("Insufficient Balance")
    else:
        balance -= amount
        print(f"The Fund is Invested in Crypto")
    return balance


@time_measure
def mobile_banking_app():
    balance = 1000
    if login():
        while True:
            print("\n Mobile Banking app")
            print("1.Transfer Money")
            print("2.Receive Money")
            print("3.Bank balance")
            print("4.Invest in Gold")
            print("5.Invest In Crypto")
            print("6.Exit")
            choice = input("Enter Your Choice:")

            if choice == "1":
                balance = transfer_money(balance)
                break
            elif choice == "2":
                balance = receive_money(balance)
            elif choice == "3":
                balance = bank_balance(balance)
            elif choice == "4":
                balance = invest_in_gold(balance)
            elif choice == "5":
                balance = invest_in_crypto(balance)
            elif choice == "6":
                print("Thanks For Visiting")
                break
            else:
                print("Invalid Choice")

mobile_banking_app()



