import streamlit as st
import os
import user_inputs

my_file = "todo.txt"
if not os.path.exists(my_file):
    with open(my_file, "w") as file:
        pass

todos = user_inputs.get_input(my_file)


def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    user_inputs.write_todos(todos, my_file)


st.title("My Web TODO App!!!")
st.subheader("Enter the todo item")
st.write("This app is your reminder!!!")

st.checkbox("Write anything")

for index, todo_item in enumerate(todos):
    checkbox = st.checkbox(todo_item, key=todo_item)
    if checkbox:
        todos.pop(index)
        del st.session_state[todo_item]
        user_inputs.write_todos(todos, my_file)
        st.experimental_rerun()

st.text_input(label="New Todo", placeholder="Add a todo!!!",
              on_change=add_todo, key="new_todo")


st.session_state