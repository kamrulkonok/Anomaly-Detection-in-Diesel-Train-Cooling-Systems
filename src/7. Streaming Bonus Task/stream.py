import streamlit as st  # web development
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import time  # to simulate a real time data, time loop
import plotly.express as px  # interactive charts
from sqlalchemy import create_engine


# Database connection parameters
dbname = 'DataMining'
user = 'postgres'
password = 'datamining'
host = 'localhost'  # localhost or the server address
port = '5433'  # default PostgreSQL port is 5432

# Establish a connection to the database
connection_str = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
engine = create_engine(connection_str)

# Define the time frame for the query
start_time = '2023-01-01 00:00:00'  # Replace with your start time
end_time = '2023-01-30 23:59:59'    # Replace with your end time

# Define the query with placeholders for time frame parameters
query_time_frame = f"""
SELECT *
FROM vehicle_data
WHERE timestamps_UTC BETWEEN '{start_time}' AND '{end_time}'
ORDER BY timestamps_UTC ASC;
"""

# Execute the query and store the results in a DataFrame
df = pd.read_sql_query(query_time_frame, engine)


st.set_page_config(
    page_title='Real-Time SNCB Dashboard',
    page_icon='✅',
    layout='wide'
)

# dashboard title

st.title("Real-Time / Live Data Science Dashboard")

# top-level filters

train_filter = st.selectbox("Select the Train id", pd.unique(df['mapped_veh_id']))

# creating a single-element container.
placeholder = st.empty()

# dataframe filter

df = df[df['mapped_veh_id'] == train_filter]

# near real-time / live feed simulation
live_df = pd.DataFrame(columns=df.columns)

for index, row in df.iterrows():
    # add row to the current df
    live_df = pd.concat([live_df, pd.DataFrame([row])], ignore_index=True)

    # creating KPIs
    avg_temp_air = live_df['rs_e_inairtemp_pc1'].mean()  # Average air temperature
    avg_temp_water = live_df['rs_e_wattemp_pc1'].mean()  # Average water temperature
    avg_temp_oil = live_df['rs_e_oilpress_pc1'].mean()  # Average oil temperature

    with placeholder.container():
        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)

        # fill in those three columns with respective metrics or KPIs
        kpi1.metric(label="Air temperature ", value=round(avg_temp_air))
        kpi2.metric(label="Oil temperature", value=round(avg_temp_oil))
        kpi3.metric(label="Water temperature", value=round(avg_temp_water))


        # create two columns for charts

        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### Average Air Temperature Over Time")
            fig = px.line(live_df, y='rs_e_inairtemp_pc1')
            st.write(fig)
        with fig_col2:
            st.markdown("### Location from the Most Recent Data Entries")

            # Select the last three entries of the live DataFrame
            last_entries = live_df.tail(3)

            # Check if there are enough entries
            if len(last_entries) >= 3:
                # Create a map with the last three points and connect them with a line
                map_fig = px.line_mapbox(
                    last_entries, lat='lat', lon='lon',
                    zoom=10, height=300,
                    color_discrete_sequence=["red"]  # Set the line color to red
                )

                # Add scatter points to the map for better visibility
                map_fig.add_scattermapbox(
                    lon=last_entries['lon'],
                    lat=last_entries['lat'],
                    mode='markers',
                    marker=dict(size=10, color='blue'),  # Change size and color as needed
                )

                # Update the layout of the map
                map_fig.update_layout(mapbox_style="open-street-map")
                map_fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

                # Display the map in Streamlit
                st.plotly_chart(map_fig)
            else:
                st.write("Not enough location data available for plotting.")

        st.markdown("### Detailed Data View")
        st.dataframe(df)
        time.sleep(1)
    # placeholder.empty()