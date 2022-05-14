
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

import plotly.express as px



# here is how to create containers
header_container = st.beta_container()
stats_container = st.beta_container()	
#######################################



with header_container:

	st.image('logo.png')

	st.title("DASHBOARD FOR TELECOMMUNICATION INDUSTRY ANALYTICS")




def plot_scatter(df: pd.DataFrame, x_col: str, y_col: str, title: str) -> None:
    plt.figure(figsize=(12, 7))
    sns.scatterplot(data = df, x=x_col, y=y_col)
    plt.title(title, size=20)
    plt.xticks(fontsize=14)
    plt.yticks( fontsize=14)
    plt.show()





# Another container
with stats_container:


	data = pd.read_csv('data/user_overview_data.csv')

	data.head()
	st.write(data.head(10))

	fig = plot_scatter(data.sample(300), x_col="Gaming_UL_and_DL_(Bytes)", y_col='Total_UL_and_DL_(Bytes)',
				 title="Total UL_DL vs Gaming_UL_and_DL_(Bytes)")

	st.write(fig)
	fig2 = px.scatter(data.sample(300), x_col="Gaming_UL_and_DL_(Bytes)", y_col='Total_UL_and_DL_(Bytes)', size= "pop",color="continent", title="Total UL_DL vs Gaming_UL_and_DL_(Bytes)")

	st.write(fig2)







