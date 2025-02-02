import os



def print_directory_contents(path):
    try:
        contents = os.listdir(path)
        print(f"Contents of {path} :")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"Directory {path} not found:")
print_directory_contents("/")

