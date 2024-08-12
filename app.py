import streamlit as st
import pandas as pd
import plotly.express as px


file_path = 'cars_app'
df = pd.read_csv(file_path)

st.header('Car market prices dashboard')

# Checkbox to show/hide scatter plots
show_scatter_odo = st.checkbox('Show Price vs. Odometer Scatter Plot', value=True)
show_scatter_model = st.checkbox('Show Price vs. Model Year Scatter Plot', value=True)
show_scatter_days = st.checkbox('Show Price vs. Days Listed Scatter Plot', value=True)

# Scatter plot: Price vs. Odometer
if show_scatter_odo:
    scatter_odo_fig = px.scatter(df, x='odometer', y='price', color='condition',
                                title='Price vs. Odometer by Condition',
                                labels={'odometer': 'Odometer (miles)', 'price': 'Price', 'condition': 'Condition'})
    st.plotly_chart(scatter_odo_fig)

# Scatter plot: Price vs. Model Year
if show_scatter_model:
    scatter_model_fig = px.scatter(df, x='model_year', y='price', color='model',
                                   title='Price vs. Model Year by Car Model',
                                   labels={'model_year': 'Model Year', 'price': 'Price', 'model': 'Car Model'})
    st.plotly_chart(scatter_model_fig)

# Scatter plot: Price vs. Days Listed
if show_scatter_days:
    scatter_days_fig = px.scatter(df, x='days_listed', y='price',
                                  title='Price vs. Days Listed',
                                  labels={'days_listed': 'Days Listed', 'price': 'Price'},
                                  color='condition')
    st.plotly_chart(scatter_days_fig)

# Histogram: Distribution of Fuel Types
fuel_hist_fig = px.histogram(df, x='fuel', color='fuel',
                             title='Distribution of Fuel Types',
                             labels={'fuel': 'Fuel Type'})
st.plotly_chart(fuel_hist_fig)

# Histogram: Distribution of Car Models
model_counts = df['model'].value_counts().index.tolist()
model_hist_fig = px.histogram(df, x='model', color='model',
                              category_orders={'model': model_counts},
                              title='Car Model Distribution')
model_hist_fig.update_layout(xaxis_title='Car Model', yaxis_title='Count')
st.plotly_chart(model_hist_fig)

# Bar Plot: Average Days Listed by Model
avg_days_listed = df.groupby('model')['days_listed'].mean().reset_index().sort_values('days_listed')
avg_days_fig = px.bar(avg_days_listed, x='model', y='days_listed', color='model',
                     title='Avg Days Listed by Model',
                     labels={'days_listed': 'Avg Days Listed'})
st.plotly_chart(avg_days_fig)

# Bar Plot: Average Price by Model
avg_price_by_model = df.groupby('model')['price'].mean().reset_index()
avg_price_by_model.columns = ['model', 'price']
avg_price_by_model = avg_price_by_model.sort_values(by='price')
avg_price_fig = px.bar(avg_price_by_model, x='model', y='price', color='model',
                      title='Average Price by Car Model',
                      labels={'model': 'Car Model', 'price': 'Average Price'},
                      color_discrete_sequence=px.colors.qualitative.Plotly)
avg_price_fig.update_layout(xaxis_title='Car Model', yaxis_title='Average Price',
                            xaxis_tickangle=-45)
st.plotly_chart(avg_price_fig)
