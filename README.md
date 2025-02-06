# TransitTrend: Urban Mobility Demand Forecasting

## Overview
TransitTrend is a big data solution that forecasts real-time demand for urban mobility rentals. By fusing historical rental data with live inputs—weather, traffic, and events—and processing them using Apache Spark and Kafka, it enables rental companies to optimize fleet management and reduce costs.

## Key Features
- **Real-Time Streaming:** Ingests live data via Kafka.
- **Scalable Processing:** Uses Apache Spark to handle large datasets.
- **Predictive Modeling:** Evaluates regression models (e.g., Decision Tree with RMSE: 589.60 and R²: 0.618) to forecast demand.
- **Interactive Dashboard:** Offers visual insights with a Streamlit app and Plotly charts.

## Technologies Used
- Python, Apache Spark (MLlib), Kafka, Streamlit, Plotly

## Data and Methodology
- **Data Sources:** Citi Bike rental dataset (historical and real-time via GBFS API).
- **Processing:** Merges and cleans data in Spark; creates time-based features.
- **Modeling:** Compares multiple regression models to choose the best predictor.
- **Visualization:** Displays forecasts and insights via an interactive dashboard.

## Getting Started

### Prerequisites
- Python 3.8+
- Apache Spark and Kafka installed and configured
- Familiarity with Jupyter Notebook and Streamlit

### Installation
1. **Clone the Repository**
git clone https://github.com/yourusername/TransitTrend.git
cd TransitTrend
2. **Setup Virtual Environment**
- macOS/Linux:
  ```
  python -m venv venv
  source venv/bin/activate
  ```
- Windows:
  ```
  python -m venv venv
  venv\Scripts\activate
  ```
3. **Install Dependencies**
pip install -r requirements.txt

### Running the Project
- **Data Processing & Model Training:**  
Open and run `main.ipynb` to preprocess data and train forecasting models.

- **Real-Time Data Ingestion Demo:**  
Use `kafkarealtimeconsumer.ipynb` to see how live rental data is consumed and appended to a DataFrame.

- **Dashboard:**  
Launch the interactive dashboard:
streamlit run streamlit_app.py

## Contributing
Contributions are welcome! To contribute:
- Fork the repository.
- Create a new branch and commit your changes.
- Push to your fork and open a pull request.

## License
Distributed under the MIT License.

## Acknowledgments
Special thanks to our mentors and resources that inspired this project.
