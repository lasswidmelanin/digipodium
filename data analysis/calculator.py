import streamlit as st

st.title('CALCULATOR')
st.markdown("Welcome to my first Streamlit App 😎")

c1 , c2 =st.columns(2)
fnum=c1.number_input("Enter first number")
snum=c2.number_input("Enter second number")

options = ['Add','Subtract','Multiplication','Division']
choice = st.radio("Select an operation",options,horizontal=True)

button = st.button("Calculate")

if button:
    if choice == 'Add':
        result = fnum + snum
    if choice == 'Subtract':
        result = fnum - snum
    if choice == 'Multiplication':
        result = fnum * snum
    if choice == 'Division':
        result = fnum / snum
st.success(f'result is {result}')