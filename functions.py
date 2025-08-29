FIlEPATH = "todos.txt"

def get_todos(filepath = FIlEPATH):
    """Read a text file and return the list of todos."""
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local

def write_todos( todos_list, filepath = FIlEPATH):
    """Write a list of todos to a text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_list)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())