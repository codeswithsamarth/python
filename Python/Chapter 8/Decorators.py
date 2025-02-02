# Decorator is a function that takes another function as a argument modifies it return it
#                     or

# The functions that extends behaviour of another Function Without changing the Base Function

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

@time_measure
def square(numbers):
    result = []
    result.append(numbers * numbers)
    print(result)
square(11)


def login_authenticate(func):
    _username = "Samarthp1234"
    _password = "SAMA_2008"

    def wrapper(user_id, password):
        if user_id == _username and password == _password:
                return func(user_id)
        else:
            print("Login Credential fail ")
            return None

    return wrapper

@login_authenticate
def login(user_id):
    print(f"Welcome {user_id}")

login("Samarthp1234","SAMA_2008")


def require_admin_permission(func):
    def wrapper(user,user_to_delete,*args,**kwargs):
        if user.get("role") == "admin":
            return func(user_to_delete,*args,**kwargs)
        else:
            print("Authentic Failed")
            return None
    return wrapper


def delete_user(user_to_delete):
    print(f"User {user_to_delete} has been deleted")


admin_user = {"Name":"Samarth","role":"Admin"}

delete_user(admin_user,"Charlie")

