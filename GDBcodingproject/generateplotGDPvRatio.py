import pandas as pd
import matplotlib.pyplot as plt


gdp = pd.read_csv("gdp_clean.csv")
ratio = pd.read_csv("labor_ratio_clean.csv")

gdp["delta_gdp"] = gdp.groupby("Country Code")['GDP'].diff()
ratio["delta_ratio"] = ratio.groupby("Country Code")['Ratio'].diff()



df = gdp[["Country Name", "Country Code","Year","delta_gdp"]].merge(
    ratio[["Country Name", "Country Code","Year","delta_ratio"]],
    on=["Country Name","Country Code","Year"],
    how="inner"
).dropna(subset=["delta_gdp","delta_ratio"]).reset_index()

df.drop(['index'], axis=1, inplace=True) 

df.to_csv("merged.csv", index=False)

# dropdown = Dropdown(options=countries, description="Country:", value=countries[0])

# def plot_country(country_name):
#     d = df[df["Country Name"] == country_name].sort_values("Year")
#     plt.figure(figsize=(8, 4))
#     plt.plot(df["Year"], df["delta_gdp"], label="Δ GDP")
#     plt.plot(df["Year"], df["delta_ratio"], label="Δ Ratio")
#     plt.title(country_name)
#     plt.grid(True)
#     plt.xlabel("Year")
#     plt.ylabel("Change")
#     plt.legend()
#     plt.grid(True)
#     plt.show()

# country = input("Enter country name (exact): ")
# d = df[df["Country Name"] == country].sort_values("Year")
# print(d)

# plt.figure(figsize=(8,4))
# plt.plot(d["Year"].to_numpy(), d["delta_gdp"].to_numpy(), label="Change in GDP from previous year")

# plt.plot(d["Year"].to_numpy(), d["delta_ratio"].to_numpy(), label="Change in the ratio of female to male laborers from previous year")
# plt.title(country)
# plt.xlabel("Year")
# plt.ylabel("Change Overtime")
# plt.legend(loc= "upper left")
# plt.show()

# print(gdp.head(20))
# print("""

# """)
# print(ratio.head(33))
# print("""

# """)
# print(df.head(10))
