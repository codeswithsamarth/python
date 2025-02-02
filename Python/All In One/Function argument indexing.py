def multiply(a,b,c=1):
    print(a*b*c)

multiply(11,22)

def print_dimensions(dimensions):
    print(f"Length : {dimensions[0]} Breadth : {dimensions[1]} Height {dimensions[2]} ")

print_dimensions([11,22,33])


def email_domain_check():
    domain1 = "@gmail.com"
    domain2 = "@yahoo.com"
    domain3 = "@hotmail.com"

    valid = "Email Format Valid"
    email = input("Enter Your Email:")
    if domain1 in email:
        print(email,valid)
    elif domain2 in email:
        print(email,valid)
    elif domain3 in email:
        print(email,valid)
    else:
        print("The Email is invalid")


