#custom functions to reduce repetitive code
FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH): #function with parameter "filepath"
    """Read a text file and return the list of
     to-do items.
     """ #doc-string - can be called with help to see what teh function means (custom help) also recognises breaklines
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()  # ensures file closes after this line
    return todos_local


def write_todos(todos_arg,filepath=FILEPATH): #just write information, no return
    """write the to-do items list in the text file."""
    with open(filepath, "w") as file:
          file.writelines(todos_arg)