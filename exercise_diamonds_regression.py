import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd
import joblib

st.title("Diamond Pricing App")
st.write("From the diamond data, we built a machine learning model for pricing of the diamond")

#dataframe
df = pd.read_csv("diamonds_regression.csv")

#Sidebar that toggle show/hide dataframe
st.sidebar.title("Hide aor Show Dataframe")
option_sidebar = st.sidebar.selectbox("How would you like to Hide or Show Dataframe?", ('Show', 'Hide'))

if option_sidebar is 'Show':
    st.header("Dataframe")
    st.write(df.head(20))
st.sidebar.title("Diamond Pricing Parameters")
st.sidebar.write("Tweak to change predictions")

#ML for Diamond Price Predictions
#Carat
carat = st.sidebar.slider("Carat", 0.0, 3.0, 0.55)

#Cut
cut = st.sidebar.slider("Cut", 0, 5, 1 )

#Clarity
clarity = st.sidebar.slider("Clarity", 0.0, 8.0, 2.0 )

#Depth
depth = st.sidebar.slider("Depth", 0.0, 100.0, 61.6 )

#Table
table = st.sidebar.slider("Table", 0.0, 100.0, 55.1 )

#X
x = st.sidebar.slider("X", 0.0, 9.0, 3.97)

#Y
y = st.sidebar.slider("Y", 0.0, 9.0, 3.99)

#Z
z = st.sidebar.slider("Z", 0.0, 9.0, 2.43)
    
#Color
color = st.sidebar.selectbox("Color", ['D', 'E', 'F', 'G', 'H', 'I', 'J'])

color = 'D'
if color == 'D':
    col_list = [1, 0, 0, 0, 0, 0, 0]
elif color == 'E':
    col_list = [0, 1, 0, 0, 0, 0, 0]
elif color == 'F':
    col_list = [0, 0, 1, 0, 0, 0, 0]
elif color == 'G':
    col_list = [0, 0, 0, 1, 0, 0, 0]
elif color == 'H':
    col_list = [0, 0, 0, 0, 1, 0, 0]
elif color == 'I':
    col_list = [0, 0, 0, 0, 0, 1, 0]
elif color == 'J':
    col_list = [0, 0, 0, 0, 0, 0, 1]
    
    
#Main Page
st.subheader("Predictions")

#Loading the model
filename = 'diamond_regression_model.sav'
loaded_model = joblib.load(filename)

#Prediction
prediction = round(loaded_model.predict([[carat, cut, clarity, depth, table, x, y, z] + col_list ])[0])
st.write(f"Suggested Diamond Price is: {prediction}")
    
#Chart
#Scatterplot
sns.scatterplot(data=df, x=df.carat, y=df.price, color="blue")
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)

#Displot
sns.displot(df.carat - df.price, color="green")
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)

plt.hist(df.price)
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)