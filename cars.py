import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

st.title('Comparaison des voitures !')
st.write("Modèles américains, européens et japonais")

# name = st.text_input("Please give me your name :")
# name_length = len(name)
# st.write("Your name has ",name_length,"characters")


link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)
df_cars.head()


# st.write(df_weather) # pour afficher 
# # df_weather de manière informelle ça 

# st.line_chart(df_weather['MAX_TEMPERATURE_C'])


# viz_correlation = sns.heatmap(df_weather.corr(), 
# 								center=0,
# 								cmap = sns.color_palette("vlag", as_cmap=True)
# 								)

# st.pyplot(viz_correlation.figure)

# # pour plotly utiliser : st.plotly_chart() à la place de st.pyplot()

import plotly.express as px
mpg = px.box(df_cars, x="continent", y="mpg", points="all",
color='continent', color_discrete_sequence=["red", "blue", "grey"],
title="MPG per continent",category_orders={"continent": ["US", "Europe", "Japan"]})
st.plotly_chart(mpg)

import plotly.express as px
cubicinches = px.box(df_cars, x="continent", y="cubicinches", points="all",
color='continent', color_discrete_sequence=["red", "blue", "grey"],
title="Cubic inches per continent",category_orders={"continent": ["US", "Europe", "Japan"]})
st.plotly_chart(cubicinches)

import plotly.express as px
hp = px.box(df_cars, x="continent", y="hp", points="all",
color='continent', color_discrete_sequence=["red", "blue", "grey"],
title="Horse power per continent",category_orders={"continent": ["US", "Europe", "Japan"]})
st.plotly_chart(hp)

# import plotly.express as px
# fig = px.box(df_cars, x="continent", y="weightlbs", points="all",
# color='continent', color_discrete_sequence=["red", "blue", "green"],
# title="Weightlbs per continent",category_orders={"continent": ["US", "Europe", "Japan"]})
# fig.show()

# import plotly.express as px
# fig = px.box(df_cars, x="continent", y="time-to-60", points="all",
# color='continent', color_discrete_sequence=["red", "blue", "green"],
# title="Weightlbs per continent",category_orders={"continent": ["US", "Europe", "Japan"]})
# fig.show()



f_comptage = df_cars.groupby(['mpg','continent']).size().reset_index(name='COUNT')

histo_comptage_mpg = px.histogram(f_comptage, x="mpg", y="COUNT", color="continent",
                   marginal="box", color_discrete_sequence=["red", "blue", "grey"],# or violin, rug
                   hover_data=f_comptage.columns)
st.plotly_chart(histo_comptage_mpg)


cmap = sns.diverging_palette(220, 20, center='light', as_cmap=True)
car_heatmap = sns.heatmap(df_cars.corr(), vmin=-1, vmax=1, cmap=cmap,annot=True) #vmin et vmax pour centrer les couleurs sur 0
car_heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':12}, pad=12)
st.pyplot(car_heatmap.figure)