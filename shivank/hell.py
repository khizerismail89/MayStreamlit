import streamlit as st

st.write("""
# My first app
Hello *world!*
""")

number = st.slider("Pick a number", 0, 100)

st.header("this is a header")

st.title("this is title")

agree = st.checkbox("IS your instructor awesome or not")

if agree:
    st.write("YEs, he is!!")


genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

def sqr(num):
    return num*num

num = st.number_input("insert a number")
if(st.button("calculate square")):
    result = sqr(num)
    st.text(result)

