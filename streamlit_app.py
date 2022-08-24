
import streamlit
import pandas
import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_curwh = my_cnx.cursor()
my_curwh.execute("use warehouse compute_wh")
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title('Diner! new menu! blahblahbalh')

streamlit.header('Breakfast Favorites')
streamlit.text('Omega 3 & Blueberry Oatmeal 🥣')
streamlit.text('Kale, Spinach & rocket smoothie.  Blech')
streamlit.text('Hard Boiled Free range egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# new section
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)


# new variable
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# dataframe it!
streamlit.dataframe(fruityvice_normalized)
