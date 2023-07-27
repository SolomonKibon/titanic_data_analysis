import streamlit as st
import pandas as pd 
import plotly.express as px

st.subheader('Solomon Kibon')

#heading and brief description
st.title('Titanic Data Analysis')
st.write("This app analyzes the Titanic dataset and displays various visualizations.")
#Load the dataset and preprocess it (as shown in the previous response):
@st.cache_data
def load_data():
    data='titanic.csv'
    data = pd.read_csv(data)
    data.drop('Unnamed: 0',axis=1,inplace=True)
    data['Age'].fillna(data['Age'].median(), inplace=True)
    data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
    data.drop('Cabin', axis=1, inplace=True)
    data['FamilySize'] = data['SibSp'] + data['Parch'] + 1
    data['IsAlone'] = data['FamilySize'].apply(lambda x: 1 if x == 1 else 0)
    return data

data = load_data()
#Display the data
if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(data)

#Create the visualizations using Plotly and display them in the app:
#Survival rate by gender:
pclass_survival = data.groupby('Pclass')['Survived'].mean().reset_index()
fig_pclass_survival = px.bar(pclass_survival, x='Pclass', y='Survived', title='Survival Rate by Passenger Class')
st.plotly_chart(fig_pclass_survival)
#Survival rate by passenger class
pclass_survival = data.groupby('Pclass')['Survived'].mean().reset_index()
fig_pclass_survival = px.bar(pclass_survival, x='Pclass', y='Survived', title='Survival Rate by Passenger Class')
st.plotly_chart(fig_pclass_survival)

#Age distribution of passengers
fig_age_survival = px.histogram(data, x='Age', color='Survived', nbins=50, title='Age Distribution by Survival Status')
st.plotly_chart(fig_age_survival)
#Age distribution by survival status:
fig_age_survival = px.histogram(data, x='Age', color='Survived', nbins=50, title='Age Distribution by Survival Status')
st.plotly_chart(fig_age_survival)