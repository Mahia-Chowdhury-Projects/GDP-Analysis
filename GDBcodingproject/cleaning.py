import pandas as pd
import pycountry

#CLEANING GDP
df_GDP=  pd.read_csv("GDPData.csv")

new_columns = [int(item) if isinstance(item, float) else item for item in df_GDP.iloc[2].tolist()]

df_GDP.columns = new_columns
df_GDP = df_GDP.iloc[3:].reset_index()

#take out columns we dont want 
# df_GDP.drop(['Indicator Name','Indicator Code'], axis=1, inplace=True) 
df_GDP = df_GDP.drop(columns=df_GDP.columns[3:35])

valid_iso3 = [country.alpha_3 for country in pycountry.countries]
valid_iso3.append('WLD')
df_GDP = df_GDP[df_GDP['Country Code'].isin(set(valid_iso3))].reset_index(drop=True)

df_GDP.drop(['index'], axis=1, inplace=True) 

df_GDP = pd.melt(df_GDP, id_vars=['Country Code', "Country Name"], var_name = "Year", value_name="GDP")

df_GDP = df_GDP.sort_values(by=['Country Name', 'Year'])

print(df_GDP.head(300))
print(df_GDP.shape)
print('''



''')

#CLEANING GII
df_GII = pd.read_csv("GenderInequalityIndex.csv")

#only for 2023
df_GII = df_GII.iloc[:,[1,2]]

new_columns2 = ["Country", "GII"]
df_GII.columns = new_columns2
df_GII = df_GII.sort_values(by = "Country").reset_index(drop=True)

df_GII = df_GII.iloc[7:].reset_index(drop=True)
iso3_codes = []

for name in df_GII["Country"].tolist():
    try:
        # Find by name (case-insensitive)
        country = pycountry.countries.search_fuzzy(name)[0]
        iso3_codes.append(country.alpha_3)
    except:
        iso3_codes.append(None)



df_GII.insert(loc=1, column='Country Code', value=iso3_codes)

df_GII = df_GII[df_GII['Country Code'].isin(set(valid_iso3))].reset_index()

df_GII.drop(['index'], axis=1, inplace=True) 

# print(df_GII.columns.to_list)
# print(df_GII.head(20))
print('''



''')
#Ratio of female to male labor force participation rate CLEANING 
df_ratio = pd.read_csv('ratio.csv')

new_columns = [int(item) if isinstance(item, float) else item for item in df_ratio.iloc[2].tolist()]

df_ratio.columns = new_columns
df_ratio = df_ratio.iloc[3:].reset_index(drop=True)

# Drop them all at once
years_to_drop = [year for year in range(1960, 1990)] 
df_ratio = df_ratio.drop(columns=years_to_drop)

df_ratio = df_ratio[df_ratio['Country Code'].isin(set(valid_iso3))].reset_index()
df_ratio.drop(['index','Indicator Name', 'Indicator Code'], axis=1, inplace=True) 

df_ratio = pd.melt(df_ratio, id_vars=['Country Code', "Country Name"], var_name = "Year", value_name="Ratio")
df_ratio = df_ratio.sort_values(by=['Country Name', 'Year'])

# print(df_ratio.columns.to_list)
print(df_ratio.head(20))

df_GDP.to_csv("gdp_clean.csv", index=False)
df_GII.to_csv("gii_clean.csv", index=False)
df_ratio.to_csv("labor_ratio_clean.csv", index=False)
