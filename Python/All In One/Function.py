# Function is a group of statement performing a specific task

def avg():
    a = int(input("Enter Number 1:"))
    b = int(input("Enter Number 2:"))
    c = int(input("Enter Number 3:"))
    average = (a+b+c)/3
    print(average)


def calculator():
    operator = input("Enter Your Operator (+,-,*/):")
    num1 = int(input("Enter Number 1:"))
    num2 = int(input("Enter Number 2:"))
    num3 = int(input("Enter Number 3:"))
    if operator == "+":
        print(num1+num2+num3)
    elif operator == "-":
        print(num1-num2-num3)
    elif operator == "*":
        print(num1*num2*num3)
    elif operator == "/":
        if num2 == 0 or num3 == 0:
            print("Cannot divide by zero")
        else:
            print(num1/num2/num3)
    else:
        print("Invalid operator")




# To make Atm
# Atm = check balance deposit withdraw exit

def show_menu():
    print("1.Check Balance")
    print("2.Deposit Money")
    print("3.Withdraw Balance")
    print("4.Exit")

balance = 1000
def check_balance(balance):
    print(f"Your balance is ${balance}")


def Deposit_Money(balance):
    amount = float(input("Enter amount to deposit:"))
    balance += amount
    print(f"The ${amount} deposited New Balance is {balance}")

def Withdraw_balance(balance):
    amount = float(input("Enter amount to withdraw:"))
    if amount > balance:
        print("Insufficient Funds")
    else:
        balance -= amount
        print(f"The Amount ${amount} Successfully Withdraw New balance {balance}")




def Atm():
    while True:
        show_menu()
        break
    choice = input("Enter Your choice:")

    if choice == "1":
        check_balance(balance=balance)
    elif choice == "2":
        Deposit_Money(balance=balance)
    elif choice == "3":
        Withdraw_balance(balance=balance)
    elif choice == "4":
        print("Thank You for visiting Python Atm")
    else:
        print("Invalid Option")

Atm()

