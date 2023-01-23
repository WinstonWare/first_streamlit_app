import streamlit
import pandas

streamlit.title('My Parents new Healthy Diner')
streamlit.header('🥑 Breakfast Menu')
streamlit.text('🍝 Omega 3 Blueberry and Oatmeal')
streamlit.text('🥬 Kale, spinach, rocket smoothy')
streamlit.text('🥚 Hard-Boiled free-range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
