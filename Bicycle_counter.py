#Importing libraries

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.audio_input("c:\Users\donei\OneDrive\Documents\Sound Recordings\Recording (2).m4a")


#Adding a Title to my App

st.title("🚵‍♀️ Welcome to the Fremont Bicycle Counter! 🚵‍♀️")

#Adding a Gif image to my app
st.image(
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHR5MGNjd2hrdXdvZjZ5YW1jbnl0NnNhZmMzNGhqbjhhbnI5aGRqbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/d3FActtVPJ5XExEY/giphy.gif",
         width=250
)


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



# Creating Plotly charts

#Adding columns for layout
col1, col2 = st.columns(2)

with col1:
    st.subheader('Total Cyclists by Year')

# adding radio buttons
    year_option = st.radio(
    "Choose an Option",
    ["Busiest Year", "Quietest Year", "All Years"],
    horizontal=True
)


    data["Date"] = pd.to_datetime(data["Date"])
    data["Year"] = data["Date"].dt.year

        
    yearly_totals = (
        data.groupby ("Year")[
            "Fremont Bridge Sidewalks, south of N 34th St Total",
        ]
    .sum()
    .reset_index()
)

    if year_option == "Busiest Year":
        yearly_totals = yearly_totals.nlargest(
        1, "Fremont Bridge Sidewalks, south of N 34th St Total"
    )

    elif year_option == "Quietest Year":
        yearly_totals = yearly_totals.nsmallest(1, 
                                            "Fremont Bridge Sidewalks, south of N 34th St Total"
    )




    fig1 = px.bar(
    yearly_totals,
    x="Year", 
    y="Fremont Bridge Sidewalks, south of N 34th St Total",
    title="Yearly Total Cyclist Crossings",
    color_discrete_sequence=["green"]
)

    st.plotly_chart(fig1, use_container_width=True) 



with col2:
    st.subheader('Total Cyclists by Month')

    month_order = ["January", "February", "March", "April", "May", "June", 
                    "July", "August", "September", "October", "November", "December"
    ]

    data["Month"] = pd.Categorical(
    data["Month"],
    categories=month_order,
    ordered=True
    )

    data["Date"] = pd.to_datetime(data["Date"])
    data["Month"] = data["Date"].dt.month_name()
    categories=month_order,
    ordered=True



    month_option = st.radio(
    "Choose an Option",
    ["Busiest Month", "Quietest Month", "All Months"],
    horizontal=True
)

   
    data["Date"] = pd.to_datetime(data["Date"])
    data["Month"] = data["Date"].dt.month_name()
        
    monthly_totals = (
        data.groupby ("Month", observed=False)[
             "Fremont Bridge Sidewalks, south of N 34th St Total",
        ]
        .sum()
        .reset_index()
        .sort_values("Month")
)

    if month_option == "Busiest Month":
        monthly_totals = monthly_totals.nlargest(
        1, "Fremont Bridge Sidewalks, south of N 34th St Total",
    )

    elif month_option == "Quietest Month":
        monthly_totals = monthly_totals.nsmallest(1, 
                                            "Fremont Bridge Sidewalks, south of N 34th St Total",
    )




    fig2 = px.area(
    monthly_totals,
    x="Month", 
    y="Fremont Bridge Sidewalks, south of N 34th St Total",
    title="Monthly Total Cyclist Crossings",
    color_discrete_sequence=["yellow"],
    category_orders={"Month": month_order}
)

    st.plotly_chart(fig2, use_container_width=True) 


#Adding columns for layout
col3, col4 = st.columns(2)

with col3:
    st.subheader('Average Cyclists by Month')

    month_order = ["January", "February", "March", "April", "May", "June", 
                    "July", "August", "September", "October", "November", "December"
    ]

    data["Month"] = pd.Categorical(
    data["Month"],
    categories=month_order,
    ordered=True
    )
    
    data["Date"] = pd.to_datetime(data["Date"])
    data["Month"] = data["Date"].dt.month_name()
    categories=month_order,
    ordered=True
    
    month_option = st.radio(
    "Choose an Option",
    ["Busiest Average Month", "Quietest Average Month", "All Months"],
    horizontal=True
)

    data["Date"] = pd.to_datetime(data["Date"])
    data["Month"] = data["Date"].dt.month_name()

        
    average_monthly_totals = (
        data.groupby ("Month", observed=False)[
             "Fremont Bridge Sidewalks, south of N 34th St Total",
        ]
        .mean()
        .reset_index()
        .sort_values("Month")
)


    if month_option == "Busiest Average Month":
        average_monthly_totals = monthly_totals.nlargest(
        1, "Fremont Bridge Sidewalks, south of N 34th St Total"
    )

    elif month_option == "Quietest Average Month":
        average_monthly_totals = monthly_totals.nsmallest(1, 
                                            "Fremont Bridge Sidewalks, south of N 34th St Total"
    )




    fig3 = px.bar(
    average_monthly_totals,
    x="Fremont Bridge Sidewalks, south of N 34th St Total", 
    y="Month",
    title="Monthly Total Cyclist Crossings",
    color_discrete_sequence=["orange"],
    category_orders={"Month": month_order}
)

    st.plotly_chart(fig3, use_container_width=True) 



#Comparing sidewalk totals

st.subheader('East and West Sidewalk Yearly Totals')

data["Date"] = pd.to_datetime(data["Date"])
data["Year"] = data["Date"].dt.year

        
sidewalk_totals = (
        data.groupby ("Year")[
        [
        "Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk", 
        "Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk"
        ]
    ]
    .sum()
    .reset_index()
)
fig = px.bar(
    sidewalk_totals,
    x = "Year",
    y = [ 
        "Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk", 
        "Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk"
        ],
        barmode="group",
        title="West Sidewalk Vs East Sidewalk Yearly Totals",
        labels={
            "value": "yearly cyclist count", 
            "variable": "Sidewalk"
        },
        color_discrete_sequence=["blue", "red"]
    )
    
st.plotly_chart(fig, use_container_width=True)



