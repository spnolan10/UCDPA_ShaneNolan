# UCD Professional Academy - Project Submission

# 1) Real World Scenario

# Country Vaccinations data imported from Kaggle as CSV file
# Country Populations data imported from World Bank as CSV file

# 2) Importing Data

import pandas as pd
import numpy as np

country_vaccinations = pd.read_csv("country_vaccinations.csv")
print(country_vaccinations.head(), country_vaccinations.shape, country_vaccinations.info())

country_population = pd.read_csv("Country_populations.csv")
print(country_population.head(), country_population.shape, country_population.info())

# 3) Analyzing data

# Subsetting Country Vaccination data to focus on number of people vaccinated with single dose on latest date
pop_vaccinated = country_vaccinations[["Country Name", "Country Code", "date", "people_vaccinated", "vaccines"]]
print(pop_vaccinated.head())

# Groupby - sum of people vaccinated per country
vaccinated_per_country = pop_vaccinated.groupby("Country Name")["people_vaccinated"].max()
print(vaccinated_per_country.head())

# Slicing of Country Population Data to exclude incomplete 2020 population data
pop_country = country_population.loc[:, "Country Name": "2019"]

# Subsetting Country Population data to focus on 2019 population
pop_2019 = pop_country[["Country Name", "Country Code", "2019"]]
print(pop_2019.head())

# Merging of Vaccination (total people vaccinated per country) data with Population data (2019 population data)
vaccinated_per_pop = pop_2019.merge(vaccinated_per_country, on='Country Name')
print(vaccinated_per_pop.head())

# Creating a percentage of population vaccinated column
vaccinated_per_pop['Percentage_of_Pop_Vaccinated'] = (vaccinated_per_pop['people_vaccinated'] / vaccinated_per_pop['2019']*100).round(2)
vaccinated_per_pop.info()

# Create a list of EU countries
EU_Countries = {"Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czechia", "Denmark",
                "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy",
                "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal",
                "Romania", "Slovakia", "Slovenia", "Spain", "Sweden"}

# Create an EU vs Rest of the World Column
vaccinated_per_pop['EU or Rest of World'] = np.where(vaccinated_per_pop["Country Name"].isin(EU_Countries), "EU", "Rest of World")
print(vaccinated_per_pop.head())

# Groupby to compare of average of EU Vaccine rollout vs Rest of World
EU_vs_Rest_of_World = vaccinated_per_pop.groupby('EU or Rest of World'). aggregate({'2019' : 'sum', 'Percentage_of_Pop_Vaccinated': 'median'})
EU_vs_Rest_of_World2 = EU_vs_Rest_of_World.reset_index()
print(EU_vs_Rest_of_World2.head())

# Subsetting merged Vaccination and population data by EU Countries
EU_Vaccinated_per_pop = vaccinated_per_pop[vaccinated_per_pop['Country Name'].isin(EU_Countries)]
EU_Ranked = EU_Vaccinated_per_pop.sort_values('Percentage_of_Pop_Vaccinated', ascending= False)
print(EU_Ranked.head())

# 5) Visualize Data

import matplotlib.pyplot as plt
import seaborn as sns

# Compare the population vaccinated percentage of the EU verses the Rest of the World
sns.barplot(x='EU or Rest of World', y='Percentage_of_Pop_Vaccinated', data=EU_vs_Rest_of_World2)
plt.title("EU vs Rest of the World")
plt.xlabel("")
plt.ylabel("Population Vaccinated (%)")
plt.show()

# Compare the population vaccinated percentage of countries within the EU
sns.set_theme(style="whitegrid")
sns.barplot(y='Country Name', x='Percentage_of_Pop_Vaccinated', data= EU_Ranked, color="royalblue")
plt.title("EU Vaccination Rollout")
plt.xlabel("Population Vaccinated (%)")
plt.ylabel("EU Countries")
plt.show()

# 6) Data Insights

# 1) On average, approx. 7% of the EU population has been vaccinated with a single dose vs approx. 2% in the rest of the world.
# 2) In the EU, Hungary and Malta have the highest percentage of their population vaccinated with a single dose. Malta has vaccinated approx. 14% of its population.
# 3) In the EU, Latvia and Bulgaria have the lowest percentage of their population vaccinated with a vaccination rate of approx. 3.75%.
# 4) Ireland is the 7th best performing country in the EU for the rollout of Covid-19 Vaccines.
# 5) Ireland has vaccinated approx 7.5% of its population with a single dose which is just above the EU average.