import os

def list_directory_contents(directory_path):
    try:
        # Get the list of all files and directories
        contents = os.listdir(directory_path)
        
        print(f"Contents of the directory '{directory_path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{directory_path}' does not exist.")
    except NotADirectoryError:
        print(f"The path '{directory_path}' is not a directory.")
    except PermissionError:
        print(f"Permission denied to access the directory '{directory_path}'.")

# Example usage:
directory_path = input("Enter the directory path: ")
list_directory_contents(directory_path)
