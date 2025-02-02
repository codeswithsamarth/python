a = int(input("Enter Your Age :"))
if (a%2 == 0):
    print("a is even")
if(a>=18):
    print("You are above the age of consent ")
    print("Good for You")
elif(a<0):
    print("You Are Writing Invalid Age")
elif(a==0):
    print("You Are Entering 0 Which Is Not Valid Age")

else:
    print("You are Below the age of consent")
