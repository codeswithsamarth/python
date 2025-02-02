#Directory Path Access Os Module
import os
def print_directory_contents(path):
    """
    Print the contents of a directory
    """
    try:
        contents = os.listdir(path)
        print(f"Contents of {path}:")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"Directory {path} not found")

# Example usage:
print_directory_contents("/")



