marks1 = int(input("Enter Marks 1"))
marks2 = int(input("Enter Marks 2"))
marks3 = int(input("Enter Marks 3"))

total_percentage = (100*(marks1 + marks2 + marks3)/300)
if total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33:
    print("You are Passed",total_percentage,)
else:
    print("You Failed Exam",total_percentage)

