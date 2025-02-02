# a1 = int(input("Enter Number 1:"))
# a2 = int(input("Enter Number 2:"))
# a3 = int(input("Enter Number 3:"))
# a4 = int(input("Enter Number 4:"))
#
# if (a1>a2 and a1>a3 and a1>a4):
#     print("Greatest Number is a1",a1)
# if (a2>a1 and a2>a3 and a2>a4):
#     print("Greatest Number is a2",a2)
# if (a3>a1 and a3>a2 and a3>a4):
#     print("Greatest Number is a3",a3)
# if (a4>a1 and a4>a2 and a4>a3):
#     print("Greatest Number is a4",a4)

# marks1 = int(input("Enter Marks 1:"))
# marks2 = int(input("Enter Marks 2:"))
# marks3 = int(input("Enter Marks 3:"))
#
# total_percentage = 100*(marks1+marks2+marks3)/300
#
# if(total_percentage)>40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33:
#     print("You are Pass",total_percentage)
# else:
#     print("You are Fail",total_percentage)



# p1 = "Make a lot of money"
# p2 = "buy now"
# p3 = "subscribe this"
# p4 = "click this"
# message = input("Enter Comment:")
# if p1 in message or p2 in message or p3 in message or p4 in message:
#     print("This Message is Spam")
# else:
#     print("This Message is Not Spam")
#
# username = input("Enter Username :")
# if len(username) > 10:
#     print("The Username Contain more than 10 Character")
# else:
#     print("The Username Contain less than 10 Characters")

# name = ["Shubh","Harry","akash","ajay"]
# username = input("Enter Your Name :")
# if (username in name):
#     print("Name Found",username)
# else:
#     print("Name Not Found")

Marks = int(input("Enter Your Marks:"))
if Marks <= 100 and Marks >= 90:
    print("Grade EX")
elif Marks <= 90 and Marks >= 80:
    print("Grade A")
elif Marks <= 80 and Marks >= 70:
    print("Grade B")
elif Marks <= 70 and Marks >= 60:
    print("Grade C")
elif Marks <= 60 and Marks >= 50:
    print("Grade D")
elif Marks <= 50:
    print("Grade E")