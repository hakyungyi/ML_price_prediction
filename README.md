# E-commerce Vegetable Price Prediction

This project focuses on building a machine-learning model to predict the prices of various vegetables in Korea.
The time-series data are from Kaggle, with 01/01/2016 ~ 28/09/2020 for training and 28/09/2020 ~ 05/11/2020 for testing. 
The target vegetables for prediction are tomato, carrot, enoki, cabbage, and radish.


![streamlit](https://github.com/user-attachments/assets/ce6bc5b8-b7b5-4eb4-b3ee-a7d325e513e9)

Dashboard: https://hk-pricepredict.streamlit.app/


## Project Overview

The project follows a structured approach, starting with Exploratory Data Analysis (EDA) to understand the dataset and its underlying patterns. The following machine-learning models were used for prediction:

- **Ridge Regression**
- **Random Forest Regressor**
- **LGBM Regressor**
- **XGB Regressor**
- **MLP Regressor**

To enhance the performance of the machine-learning model, both an average model and a stacking model were applied.\
In this project, the stacking model leverages Random Forest. LGBM, and XGB to improve the predictive accuracy.


## Visualization

Streamlit was utilized to visualize the results of the data analysis and the performance of the machine learning models. The interactive app allows users to explore the model predictions and understand the data trends.

You can view the Streamlit app here: [Price Prediction App](https://hk-pricepredict.streamlit.app/)


## References

Source of data: https://www.nongnet.or.kr/front/index.do

This project was developed with guidance from an online course at METACODE.
