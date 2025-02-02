# # A function is a group of statements performing a specific task.
#
# # def avg(): # Function Definition
# #     a = int(input("Enter Your Number :"))
# #     b = int(input("Enter Your Number :"))
# #     c = int(input("Enter Your Number :"))
# #     average = (a+b+c)/3
# #     print(average)
# #
# # avg()
#
# # def calculator():
# #     operator = input("Enter Operator (+,-,*,/):")
# #     a = int(input("Enter Number 1:"))
# #     b = int(input("Enter Number 2 :"))
# #     c = int(input("Enter Number 3 :"))
# #     try:
# #         if operator == "+":
# #             print(a+b+c)
# #         elif operator == "-":
# #             print(a-b-c)
# #         elif operator == "*":
# #             print(a*b*c)
# #         elif operator == "/":
# #             print(a/b/c)
# #     except ProcessLookupError:
# #         print("Operator Invalid")
# #         return "Calculation Finished Thankyou"
# #
# # calculator()
#
#
# # Function is a group of statements performing a specific task.
#
# # def avg():
# #     a = int(input("Enter Number 1:"))
# #     b = int(input("Enter Number 2:"))
# #     c = int(input("Enter Number 3:"))
# #     average = (a+b+c)/3
# #     print(average)
# #
# # avg()
#
# def show_menu():
#     print("Welcome to Python ATM")
#     print("1. Check Balance")
#     print("2. Deposit Money")
#     print("3. Withdraw Money")
#     print("4. Exit")
#
# show_menu()
#
# balance = 0  # Global variable to store the account balance
#
# def check_balance():
#     print(f"Your balance is: ${balance}")
#
# def deposit_money():
#     global balance
#     amount = float(input("Enter the amount to deposit: "))
#     balance += amount
#     print(f"${amount} deposited. New balance: ${balance}")
#
# def withdraw_money():
#     global balance
#     amount = float(input("Enter the amount to withdraw: "))
#     if amount > balance:
#         print("Insufficient funds!")
#     else:
#         balance -= amount
#         print(f"${amount} withdrawn. New balance: ${balance}")
#
# def atm():
#     while True:
#         show_menu()
#         choice = input("Choose an option (1-4): ")
#
#         if choice == "1":
#             check_balance()
#             break
#         elif choice == "2":
#             deposit_money()
#             break
#         elif choice == "3":
#             withdraw_money()
#             break
#         elif choice == "4":
#             print("Thank you for using Python ATM. Goodbye!")
#             break
#         else:
#             print("Invalid option, please try again.")
#
# # Start the ATM
# atm()
#
#

def show_menu():
    print("Welcome to Python Atm:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")


balance = 1000

def check_balance():
    print(f"Your Balance is {balance}")

def deposit_money():
    global balance
    amount = float(input("Enter the amount to deposit: "))
    balance += amount
    print(f"${amount} deposited. New balance: ${balance}")



def Withdraw_Money():
    global balance
    amount = float(input("Enter Amount To Withdraw:"))
    if amount > balance:
        print("Insufficient Balance")
    else:
        balance -= amount
        print(f"{amount} has Been Successfully Withdraw New Balance is {balance}")
def atm():
    while True:
        show_menu()
        choice = input("Enter Your choice:")

        if choice == "1":
            check_balance()
            break
        elif choice == "2":
            deposit_money()
            break
        elif choice == "3":
            Withdraw_Money()
            break
        elif choice == "4":
            print("Thanks for Using Python Atm Have a Nice day")
            break



Password = input("Enter Your Password To Check:").strip()
has_upper = 0
has_lower = 0
has_digit = 0
has_special = 0
special_char = ("!@#$%^&*()_+=/?|\\<>~")

if len(Password) < 8:
    print("The Password should have 8 characters")
if len(Password) > 100:
    print("The Password is too long")

for i in Password:
    if i.isupper():
        has_upper = 1
    elif i.islower():
        has_lower = 1
    elif i.isdigit():
        has_digit = 1
    elif i in special_char:
        has_special = 1


if not has_upper:
    print("The Password Should contain Uppercase Letter")
if not has_lower:
    print("The Password Should contain Lowercase Letter")
if not has_digit:
    print("The Password Should contain Digit")
if not has_special:
    print("The Password Should contain one special character")
if has_upper and has_lower and has_digit and has_special:
    print("The Password is Valid")
