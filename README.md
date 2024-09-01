# E-commerce Vegetable Price Prediction

This project focuses on predicting the prices of various vegetables in Korea using time-series data from Kaggle. The dataset includes prices from 2016/01/01 to 2020/09/28 for training and 2020/09/29 to 2020/11/05 for testing. The target vegetables for prediction are tomatoes, carrots, enoki mushrooms, cabbages, and radishes.

source of data: https://www.nongnet.or.kr/front/index.do

![streamlit](https://github.com/user-attachments/assets/ce6bc5b8-b7b5-4eb4-b3ee-a7d325e513e9)

streamlit link - https://hk-pricepredict.streamlit.app/

## Project Overview

The project follows a structured approach, starting with Exploratory Data Analysis (EDA) to understand the dataset and its underlying patterns. The following machine learning models were used for prediction:

- **Ridge Regression**
- **Random Forest Regressor**
- **LGBM Regressor**
- **XGB Regressor**
- **MLP Regressor**

To enhance model performance, both an average model and a stacking model were applied.\
In this project, the stacking model leverages Random Forest. LGBM, and XGB to improve the predictive accuracy.

## Visualization

Streamlit was utilized to visualize the results of the data analysis and the performance of the machine learning models. The interactive app allows users to explore the model predictions and understand the data trends.

You can view the Streamlit app here: [Price Prediction App](https://hk-pricepredict.streamlit.app/)

## References

This project was developed with guidance from an online course at METACODE.
