def get_input(my_file):
    print("My File -> ", my_file)
    with open(my_file, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_local, my_file):
    """ This function writes the content of todos in a todo.txt file """
    with open(my_file, 'w') as file_local:
        file_local.writelines(todos_local)


print("Function is : ", __name__)
if __name__ == "__main__":
    print(get_input(my_file="todo.txt"))
    print(__name__)
