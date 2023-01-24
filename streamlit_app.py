import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents new Healthy Diner')
streamlit.header('🥑 Breakfast Menu')
streamlit.text('🍝 Omega 3 Blueberry and Oatmeal')
streamlit.text('🥬 Kale, spinach, rocket smoothy')
streamlit.text('🥚 Hard-Boiled free-range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
# Display the table on the page.

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
     streamlit.error("Please select a fruit to get information.")
  else:
   # streamlit.write('The user entered ', fruit_choice)
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
    streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error()


streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The Fruit load list contains:")
streamlit.dataframe(my_data_rows)

MyFruitChoice = streamlit.text_input('What fruit would you like to add?', 'Jackfruit')
streamlit.write('Thanks for adding', MyFruitChoice)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
