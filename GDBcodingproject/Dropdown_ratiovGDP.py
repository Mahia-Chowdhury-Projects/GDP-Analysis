import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np



df = pd.read_csv("merged.csv")

countries = sorted(df["Country Name"].unique())
country = st.selectbox("Choose a country", countries)



d = df[df["Country Name"] == country].sort_values("Year")

fig, ax1 = plt.subplots(figsize = (10, 4), facecolor='black')

#Left axis: 

ax1.plot(d["Year"].to_numpy(), d["delta_gdp"].to_numpy(),
        marker="o", linestyle="-", label="Change in GDP", color = 'purple')

ax1.set_xlabel('Year')
ax1.set_ylabel("Change in GDP")


ax2 = ax1.twinx()
ax2.plot(d["Year"].to_numpy(), d["delta_ratio"].to_numpy(),
        marker="o", linestyle="-", label="Change in Ratio", color = 'red')
ax2.set_ylabel("Change in Ratio")


#x-axis scale
ax1.set_xticks(d["Year"].to_numpy())
ax1.tick_params(axis="x", rotation=45)


#title
ax1.set_title(f"{country}: Year-over-year changes (Change in GDP vs Change in Ratio)")

#combine legends 

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="center left", bbox_to_anchor =  (1.05, .9))


st.pyplot(fig)