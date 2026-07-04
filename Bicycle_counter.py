#Importing libraries

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#Adding a Title to my App

st.title("🚵‍♀️ Welcome to the Fremont Bicycle Counter! 🚵‍♀️")


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



#Adding columns for layout
col1, col2 = st.columns(2)

with col1:
    st.subheader('Total Cyclists by Year')

#Drawing a histogram
    hist_values = (
        data.groupby(data[DATE_COLUMN].dt.year)[
                 'Fremont Bridge Sidewalks, south of N 34th St Total'
        ].sum()
    )

    st.bar_chart(hist_values)
    st.divider()

#Total cyclists by Month

with col2:
    st.subheader('Total Cyclists by Month')


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



#Adding columns for layout
col3, col4 = st.columns(2)

with col3:
    st.subheader('Average Cyclists by Month')

# Average number of cyclists by month

# Calculate and print mean value

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


with col4:
    st.subheader('Maximum Cyclists by Month')

# Maximum number of cyclists by month

# Calculate and print max value

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




#Comparing sidewalk totals

st.subheader('East and West Sidewalk Yearly Totals')

sidewalk_totals = (
    data.groupby(data[DATE_COLUMN].dt.year)[
        [
    
            'Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk', 
            'Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk'
        ]
    ]
    .sum()
    
)

st.area_chart(sidewalk_totals)               


# Creating Plotly charts

yearly_totals = (
        data[DATE_COLUMN] = pd.to_datetime(data["Date"])
        data["Year"] = data["Date"].dt.year
        
        yearly_totals = (
        data.groupby ("Year")[
             "Fremont Bridge Sidewalks, south of N 34th St Total",
        ]
        .sum()
        .reset_index()
)


fig = px.bar(
    yearly_totals,
    x="Year", 
    y="Fremont Bridge Sidewalks, south of N 34th St Total",
    title="Yearly Total Cyclist Crossings",
    color_continuous_scale="greens"
)

st.plotly_chart(fig, use_container_width=True) 









