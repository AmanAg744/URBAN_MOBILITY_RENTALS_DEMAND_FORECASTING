import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_lottie import st_lottie
import requests

# Function to load Lottie animations
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animation for the bike
lottie_bike = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_jcikwtux.json")

# Set page config
st.set_page_config(page_title="Bike Rental Demand Forecasting", page_icon="🚲", layout="wide")

# Title and animation
col1, col2 = st.columns([3, 1])
with col1:
    st.title("🚲 Bike Rental Demand Forecasting")
with col2:
    if lottie_bike:
        st_lottie(lottie_bike, height=150, key="bike")
    else:
        st.image("https://img.icons8.com/emoji/96/000000/bicycle-emoji.png", width=100)

st.markdown("---")

# File uploader
uploaded_file = st.file_uploader("📤 Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    st.success("File successfully uploaded!")

    # Display sample of uploaded data
    st.subheader("📊 Sample of Uploaded Data")
    st.dataframe(df.head())

    st.markdown("---")

    # Simulated prediction (replace this with your actual prediction logic)
    predictions = pd.DataFrame({
        'Day of Week': [1, 4, 6, 2, 7, 5, 3],
        'Month': [9, 9, 9, 9, 9, 9, 9],
        'Year': [2024] * 7,
        'Average Predicted Rides': [2671.94, 3325.62, 3487.62, 2566.94, 3497.62, 3387.62, 3657.62]
    })

    # Display predictions with colorful rows
    st.subheader("🔮 Predictions")
    
    def highlight_rows(row):
        if row.name % 2 == 0:
            return ['background-color: #f0f0f5']*len(row)
        else:
            return ['background-color: #e6f7ff']*len(row)

    # Apply the styling function to predictions
    st.dataframe(predictions.style.apply(highlight_rows, axis=1).set_properties(**{
        'color': '#333',
        'border-color': 'white',
        'border': '1px solid lightgrey',
        'text-align': 'center',
        'font-size': '14px',
    }))

    # Visualizations section with icon
    st.subheader("📈 Visualizations")
    st.image("https://img.icons8.com/color/96/000000/bar-chart--v1.png", width=100)

    col1, col2 = st.columns(2)

    with col1:
        # Bar chart of average predicted rides by day of week
        fig1 = px.bar(predictions, x='Day of Week', y='Average Predicted Rides', 
                      title='Average Predicted Rides by Day of Week',
                      labels={'Day of Week': 'Day of Week', 'Average Predicted Rides': 'Average Predicted Rides'},
                      color='Average Predicted Rides', color_continuous_scale='Viridis')
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        # Line chart of average predicted rides over time with graphical markers
        fig2 = px.line(predictions, x='Month', y='Average Predicted Rides', color='Day of Week',
                       title='Average Predicted Rides Over Time',
                       labels={'Month': 'Month', 'Average Predicted Rides': 'Average Predicted Rides', 'Day of Week': 'Day of Week'},
                       markers=True)
        fig2.update_traces(marker=dict(size=12, symbol="circle-open-dot", line=dict(width=2)))
        st.plotly_chart(fig2, use_container_width=True)

    # Insights section with icon
    st.subheader("💡 Insights")
    st.image("https://img.icons8.com/color/96/000000/idea.png", width=100)

    max_day = predictions.loc[predictions['Average Predicted Rides'].idxmax(), 'Day of Week']
    max_rides = predictions['Average Predicted Rides'].max()
    st.info(f"The busiest day of the week is day {max_day} with an average of {max_rides:.2f} predicted rides.")

    total_rides = predictions['Average Predicted Rides'].sum()
    st.success(f"The total predicted rides for the given week is {total_rides:.2f}.")

else:
    st.info("👆 Upload a CSV file to get started!")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ by TransitTrend")
