#created forst python file
import streamlit
import pandas as pd
#from emoji import emojize
streamlit.title("Vishudh Bhog!")
streamlit.header("Breakfast menu!")
streamlit.text('\N{flexed biceps} Breakfast of Champion Coders \N{flexed biceps}')
streamlit.text("Singhare ka parathan!")
streamlit.text("Vaishnav thali!")
my_fruit_df=pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
#my_fruit_df=my_fruit_df.set_index('Fruit')
streamlit.multiselect('Choose the fruit to make smoothies',list(my_fruit_df.Fruit))
streamlit.dataframe(my_fruit_df)
