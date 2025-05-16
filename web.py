import streamlit as st
import functions

todo_list = functions.get_todos()

def add_todo():
  todo = st.session_state["new_todo"] + "\n"
  todo_list.append(todo)
  functions.write_todos(todo_list)

st.title("My Todo App")
st.subheader("This is my todo app...")
st.write("This app is to incorease your productivity.")

for index, todo in enumerate(todo_list):
  checkbox = st.checkbox(todo, key=todo)
  if checkbox:
    todo_list.pop(index)
    functions.write_todos(todo_list)
    del st.session_state[todo]
    st.experimental_return()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
