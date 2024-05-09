import streamlit as st
import functions

todos = functions.get_todos()


#Session_state is the key at that point in time,need to ensure you mention key as well with input etc.
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


#where you place the lines is where it will appear on the web version
st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]


st.text_input(label="Enter a todo", placeholder="Add a new todo...", on_change=add_todo, key="new_todo")

st.session_state  #show activity on webpage

#to generate requirements file, run in terminal
# pip freeze > requirements.txt
