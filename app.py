import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

csv_file_path = 'data/streamlit_data.csv'

@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

df = load_data(csv_file_path)

if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
else:
    st.error("Date column not found in the CSV file.")

def preprocess_data(df):
    cutoff_date = pd.to_datetime('2020-09-28')
    cols_to_zero = ['carrot', 'tomato', 'enoki','cabbage', 'radish']
    df.loc[df.index > cutoff_date, cols_to_zero] = np.nan
    return df

def plot_predictions_over_time(df, vegetables, rolling_mean_window):
    fig, ax = plt.subplots(figsize=(14, 7))

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    num_colors = len(colors)

    for i, veg in enumerate(vegetables):
        ax.plot(df.index, df[veg], label=veg, linewidth=2, color=colors[i % num_colors])
        rolling_mean = df[veg].rolling(window=rolling_mean_window).mean()
        ax.plot(df.index, rolling_mean, label=f'{veg} ({rolling_mean_window}-day Rolling Mean)', linestyle='--', color=colors[i % num_colors])

    ax.set_xlabel('Date', fontsize=14)
    ax.set_ylabel('Price', fontsize=14)
    ax.legend(fontsize=12)
    ax.grid(True, color='lightgrey', linestyle='--')
    fig.tight_layout()
    st.pyplot(fig)


df = preprocess_data(df)

metric_file_path = 'data/metric_summary.csv'

metric_summary = pd.read_csv(metric_file_path)
metric_summary.set_index('product', inplace=True)

st.title('Vegetable Price Prediction Model Dashboard 🍅 🥦 🥕')
st.markdown("""
    Select vegetable, predicion model, and date on the left to display the predicted price
    """)

st.sidebar.title('Duration')
start_date = st.sidebar.date_input('Start Date', df.index.min())
end_date = st.sidebar.date_input('End Date ', df.index.max())

st.sidebar.title('Select Vegetable')
sorted_vegetables = sorted(df.columns)
vegetables = st.sidebar.multiselect('Vegetable:', sorted_vegetables)
rolling_mean_window = st.sidebar.slider('Rolling Mean Window', min_value=1, max_value=30, value=7)

filtered_df = df.loc[start_date:end_date]

if vegetables:
    st.subheader('Prediction Dashbaord')
    plot_predictions_over_time(filtered_df, vegetables, rolling_mean_window)

if st.checkbox('Show Filtered DataFrame'):
    st.write(filtered_df)

st.subheader('Accuracy Summary')
st.write(metric_summary)