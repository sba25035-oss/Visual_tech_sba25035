#Importing libraries

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#Adding a Title to my App

st.title("Bicycle Counter Dashboard")


#Fetch some data

DATE_COLUMN = "Date"

DATA_URL = ("Cleaned_Fremont_Bridge_Bicycle_Counter1.csv")


@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')

# Load rows of data into the dataframe.
data = load_data(None)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

#Inspect the raw data
show_data = st.checkbox('Show Raw Data')
if show_data:
    st.subheader('Raw data')
    st.write(data)


#Adding a subheader
st.subheader('Total Cyclists by Year')

#Drawing a histogram
hist_values = (
    data.groupby(data[DATE_COLUMN].dt.year)[
                 'Fremont Bridge Sidewalks, south of N 34th St Total'
                 ].sum()
    )

st.bar_chart(hist_values)


st.subheader('Total Cyclists by Month')

# Total number of cyclists by month

# Calculate and print sum value

month_order = ["January", "February", "March", "April", "May", "June", 
               "July", "August", "September", "October", "November", "December"
              ]
data["Month"] = pd.Categorical(
    data["Month"],
    categories=month_order,
    ordered=True
)

monthly_totals = (
    data
    .sort_values("Month")
    .groupby ("Month")["Fremont Bridge Sidewalks, south of N 34th St Total"] 
    .sum()
    .reset_index()

)

st.line_chart(monthly_totals.set_index("Month"))



st.subheader('Average Cyclists by Month')

# Average number of cyclists by month

# Calculate and print sum value

month_order = ["January", "February", "March", "April", "May", "June", 
               "July", "August", "September", "October", "November", "December"
              ]
data["Month"] = pd.Categorical(
    data["Month"],
    categories=month_order,
    ordered=True
)

average_monthly_totals = (
    data
    .sort_values("Month")
    .groupby ("Month")["Fremont Bridge Sidewalks, south of N 34th St Total"] 
    .mean()
    .reset_index()

)

st.area_chart(average_monthly_totals.set_index("Month"))



st.subheader('Maximum Cyclists by Month')

# Maximum number of cyclists by month

# Calculate and print sum value

month_order = ["January", "February", "March", "April", "May", "June", 
               "July", "August", "September", "October", "November", "December"
              ]
data["Month"] = pd.Categorical(
    data["Month"],
    categories=month_order,
    ordered=True
)

max_monthly_totals = (
    data
    .sort_values("Month")
    .groupby ("Month")["Fremont Bridge Sidewalks, south of N 34th St Total"] 
    .max()
    .reset_index()

)

st.line_chart(max_monthly_totals.set_index("Month"))



st.subheader('Minimum Cyclists by Month')

# Minimum number of cyclists by month

# Calculate and print sum value

month_order = ["January", "February", "March", "April", "May", "June", 
               "July", "August", "September", "October", "November", "December"
              ]
data["Month"] = pd.Categorical(
    data["Month"],
    categories=month_order,
    ordered=True
)

min_monthly_totals = (
    data
    .sort_values("Month")
    .groupby ("Month")["Fremont Bridge Sidewalks, south of N 34th St Total"] 
    .min()
    .reset_index()

)

st.line_chart(min_monthly_totals.set_index("Month"))
               







